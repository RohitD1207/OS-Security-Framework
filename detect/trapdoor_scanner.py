import requests
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from utils import log_alert

TARGET = "http://localhost:8080"
COMMON_TRAPDOORS = [
    "/admin",
    "/debug",
    "/hidden",
    "/supersecret",  # the one we planted
    "/backdoor",
    "/console",
    "/godmode",
]

def scan_trapdoors():
    print(f"🔎 Scanning {TARGET} for trapdoors...\n")
    for path in COMMON_TRAPDOORS:
        url = TARGET + path
        try:
            res = requests.get(url, timeout=2)
            if res.status_code == 200:
                print(f"🚨 Found open trapdoor: {url}")
                log_alert(f"TRAPDOOR FOUND → {url}")
            elif res.status_code == 403:
                print(f"🛑 Forbidden but exists: {url}")
                log_alert(f"TRAPDOOR DETECTED (403) → {url}")
            elif res.status_code == 401:
                print(f"🔐 Protected endpoint found: {url}")
                log_alert(f"TRAPDOOR DETECTED (401) → {url}")
        except requests.ConnectionError:
            print(f"❌ Connection failed: {url}")
        except requests.Timeout:
            print(f"⌛ Timeout: {url}")

if __name__ == "__main__":
    scan_trapdoors()
