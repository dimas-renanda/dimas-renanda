"""
Extreme Load Test Script - http://tridom.biz.id
Versi Windows

====================================================
CARA INSTALL (jalankan sekali saja):
====================================================
1. Install Python dari https://python.org (centang "Add to PATH")
2. Buka CMD atau PowerShell, jalankan:
     pip install locust

====================================================
CARA JALANKAN:
====================================================
Mode Web UI (buka browser ke http://localhost:8089):
  locust -f load_test_windows.py --host http://tridom.biz.id

Mode Headless keep running:
  locust -f load_test_windows.py --headless -u 500 -r 50 --host http://tridom.biz.id --run-time 0

Naik bertahap:
  -u 200  -r 20   --> warmup
  -u 500  -r 50   --> medium stress
  -u 1000 -r 100  --> heavy
  -u 2000 -r 200  --> extreme

Stop: tekan Ctrl+C
====================================================
"""

from locust import HttpUser, task, between
import random
import string


def rand_str(n=8):
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=n))


class AggressiveUser(HttpUser):
    wait_time = between(0.05, 0.2)

    @task(5)
    def hammer_homepage(self):
        for _ in range(5):
            self.client.get("/", name="[GET] /", catch_response=True)

    @task(4)
    def hit_api_endpoints(self):
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
        params = f"?v={rand_str()}&t={rand_str()}&r={random.randint(1,99999)}"
        self.client.get(f"/{params}", name="[GET] /?bypass-cache", catch_response=True)

    @task(2)
    def concurrent_static(self):
        statics = [
            "/favicon.ico", "/robots.txt", "/sitemap.xml",
            "/manifest.json", "/assets/app.js", "/assets/app.css",
        ]
        for s in random.choices(statics, k=3):
            self.client.get(s, name=f"[Static] {s}", catch_response=True)

    @task(2)
    def large_payload_post(self):
        big_payload = {
            "data": rand_str(2000),
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
        path = "/" + "/".join(rand_str(6) for _ in range(random.randint(3, 7)))
        self.client.get(path, name="[GET] deep-path", catch_response=True)
