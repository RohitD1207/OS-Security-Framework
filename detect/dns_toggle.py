import os

HOSTS_FILE = "/etc/hosts"
FAKE_ENTRY = "123.123.123.123 google.com"
MARKER = "# FAKE_GOOGLE_FOR_DEMO"

def read_hosts():
    with open(HOSTS_FILE, "r") as f:
        return f.readlines()

def write_hosts(lines):
    with open(HOSTS_FILE, "w") as f:
        f.writelines(lines)

def toggle_dns_spoof():
    lines = read_hosts()
    exists = any(MARKER in line for line in lines)

    if exists:
        print("🧹 Removing fake DNS entry for google.com...")
        lines = [line for line in lines if MARKER not in line]
    else:
        print("💉 Adding fake DNS entry for google.com...")
        lines.append(f"{FAKE_ENTRY}    {MARKER}\n")

    try:
        write_hosts(lines)
        print("✅ Done.")
    except PermissionError:
        print("❌ Permission denied. Run this script with sudo!")

if __name__ == "__main__":
    toggle_dns_spoof()
