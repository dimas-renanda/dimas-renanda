"""
Extreme Load Test Script - http://tridom.biz.id
High concurrency stress test menggunakan Locust.

Cara jalankan (headless, keep running):
  cd ~/.openclaw/workspace && source venv/bin/activate
  locust -f load_test.py --headless -u 500 -r 50 --host http://tridom.biz.id --run-time 0

Naik bertahap kalau mau lihat titik batas:
  -u 200   → warmup
  -u 500   → medium stress
  -u 1000  → heavy
  -u 2000  → extreme
"""

from locust import HttpUser, task, between, constant_pacing
import random
import string

# ─── Helper ────────────────────────────────────────────────────────────────────
def rand_str(n=8):
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=n))

# ─── User Behavior ─────────────────────────────────────────────────────────────
class AggressiveUser(HttpUser):
    # Hampir nol jeda — kirim request secepat server bisa balas
    wait_time = between(0.05, 0.2)

    @task(5)
    def hammer_homepage(self):
        """Spam homepage berkali-kali"""
        for _ in range(5):
            self.client.get("/", name="[GET] /", catch_response=True)

    @task(4)
    def hit_api_endpoints(self):
        """Coba berbagai endpoint API umum"""
        endpoints = [
            "/api", "/api/v1", "/api/v2",
            "/api/login", "/api/user", "/api/data",
            "/index.php", "/login", "/dashboard",
            "/admin", "/home", "/health",
        ]
        for ep in random.choices(endpoints, k=4):
            self.client.get(ep, name=f"[GET] {ep}", catch_response=True)

    @task(3)
    def post_requests(self):
        """POST ke endpoint umum dengan dummy payload"""
        endpoints = ["/login", "/api/login", "/api/v1/login", "/api/auth"]
        payload = {
            "username": rand_str(),
            "password": rand_str(12),
            "token": rand_str(32),
        }
        ep = random.choice(endpoints)
        self.client.post(ep, json=payload, name=f"[POST] {ep}", catch_response=True)

    @task(3)
    def query_string_flood(self):
        """GET dengan random query string (bypass cache)"""
        params = f"?v={rand_str()}&t={rand_str()}&r={random.randint(1,99999)}"
        self.client.get(f"/{params}", name="[GET] /?bypass-cache", catch_response=True)

    @task(2)
    def concurrent_static(self):
        """Hit berbagai resource statis"""
        statics = [
            "/favicon.ico", "/robots.txt", "/sitemap.xml",
            "/manifest.json", "/assets/app.js", "/assets/app.css",
        ]
        for s in random.choices(statics, k=3):
            self.client.get(s, name=f"[Static] {s}", catch_response=True)

    @task(2)
    def large_payload_post(self):
        """POST payload besar ke server"""
        big_payload = {
            "data": rand_str(2000),  # ~2KB payload
            "metadata": {f"key_{i}": rand_str(50) for i in range(20)},
        }
        self.client.post(
            "/api/submit",
            json=big_payload,
            name="[POST] Large Payload",
            catch_response=True
        )

    @task(1)
    def deep_path_flood(self):
        """Hit path panjang & random"""
        path = "/" + "/".join(rand_str(6) for _ in range(random.randint(3, 7)))
        self.client.get(path, name="[GET] deep-path", catch_response=True)
