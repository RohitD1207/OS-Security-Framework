import socket
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from utils import log_alert

TARGET_DOMAIN = "google.com"
EXPECTED_IP = "142.250.192.14"  # Placeholder; fine for demo purposes

def check_dns_poison():
    try:
        actual_ip = socket.gethostbyname(TARGET_DOMAIN)
        print(f"🌐 {TARGET_DOMAIN} resolves to: {actual_ip}")

        if actual_ip != EXPECTED_IP:
            print(f"🚨 WARNING: DNS spoofing detected!")
            print(f"    ➤ Expected: {EXPECTED_IP}")
            print(f"    ➤ Got:      {actual_ip}")
            log_alert(f"DNS SPOOF DETECTED → {TARGET_DOMAIN} resolved to {actual_ip} (expected {EXPECTED_IP})")
        else:
            print("✅ Domain is resolving to the correct IP.")
    except Exception as e:
        print(f"❌ Error resolving domain: {e}")
        log_alert(f"DNS CHECK FAILED → {TARGET_DOMAIN} | Error: {str(e)}")

if __name__ == "__main__":
    check_dns_poison()
