import subprocess
import argparse
import os
import sys
from multiprocessing import Process
import time

# --- Simulations ---
def simulate_buffer_overflow():
    print("\n🔥 Simulating buffer overflow...")
    os.system("gcc simulate/buffer_overflow.c -o simulate/vuln_program -fno-stack-protector -z execstack")
    os.system("simulate/vuln_program")

def simulate_trapdoor():
    print("\n🔥 Starting HTTP server with trapdoor...")
    from simulate.http_trapdoor import run_server
    p = Process(target=run_server)
    p.start()
    time.sleep(1)  # Give it time to spin up
    print("✅ Server started. Press Ctrl+C to stop.")
    try:
        p.join()
    except KeyboardInterrupt:
        print("🛑 Shutting down trapdoor server.")
        p.terminate()

def simulate_dns_poisoning():
    print("\n🔥 Poisoning /etc/hosts with malicious DNS entry...")
    os.system("sudo python3 detect/dns_toggle.py --poison")

# --- Detection ---
def detect_buffer_overflow():
    print("\n🧠 Running crash watcher...")
    os.system("python3 detect/crash_watcher.py")

def detect_trapdoor():
    print("\n🕵️ Scanning for suspicious HTTP endpoints...")
    os.system("python3 detect/trapdoor_scanner.py")

def detect_dns_poisoning():
    print("\n🔍 Checking DNS resolution against legit IP...")
    os.system("python3 detect/dns_checker.py")

# --- Fixes & Cleanup ---
def fix_dns():
    print("\n🧹 Restoring /etc/hosts to original state...")
    os.system("sudo python3 detect/dns_toggle.py --restore")

# --- Report Generator ---
def generate_report():
    log_file = "alerts.log"
    try:
        with open(log_file, "r") as f:
            lines = f.readlines()
    except FileNotFoundError:
        print("📭 No alerts.log file found. Looks like everything's safe (for now).")
        return

    if not lines:
        print("✅ No threats detected in logs. System seems clean.")
        return

    print("\n📝 Security Report")
    print("─────────────────────────────")
    categories = {
        "BUFFER OVERFLOW": [],
        "TRAPDOOR": [],
        "DNS SPOOF": [],
        "OTHER": []
    }

    for line in lines:
        if "BUFFER OVERFLOW" in line.upper():
            categories["BUFFER OVERFLOW"].append(line.strip())
        elif "TRAPDOOR" in line.upper():
            categories["TRAPDOOR"].append(line.strip())
        elif "DNS SPOOF" in line.upper() or "DNS" in line.upper():
            categories["DNS SPOOF"].append(line.strip())
        else:
            categories["OTHER"].append(line.strip())

    for cat, logs in categories.items():
        if logs:
            print(f"\n🔒 {cat}:")
            for log in logs:
                print(f"   • {log}")
            print("   💡 Suggested fix:", end=" ")
            if cat == "BUFFER OVERFLOW":
                print("Use safe functions (e.g., `fgets`), enable stack canaries.")
            elif cat == "TRAPDOOR":
                print("Audit hidden URLs & restrict access.")
            elif cat == "DNS SPOOF":
                print("Validate DNS responses, check /etc/hosts, use DNSSEC.")
            else:
                print("Investigate manually.")

    print("\n✅ End of report.")

# --- CLI Interface ---
def main():
    parser = argparse.ArgumentParser(description="🛡️ OS Vulnerability Simulation Framework")
    parser.add_argument("--simulate", choices=["all", "buffer", "trapdoor", "dns"], help="Run attack simulation")
    parser.add_argument("--detect", choices=["all", "buffer", "trapdoor", "dns"], help="Run detection tools")
    parser.add_argument("--fix", choices=["dns"], help="Run mitigation/cleanup tools")
    parser.add_argument("--report", action="store_true", help="Generate threat report from logs.")

    args = parser.parse_args()

    if args.simulate:
        if args.simulate == "all":
            simulate_buffer_overflow()
            simulate_trapdoor()
            simulate_dns_poisoning()
        elif args.simulate == "buffer":
            simulate_buffer_overflow()
        elif args.simulate == "trapdoor":
            simulate_trapdoor()
        elif args.simulate == "dns":
            simulate_dns_poisoning()

    if args.detect:
        if args.detect == "all":
            detect_buffer_overflow()
            detect_trapdoor()
            detect_dns_poisoning()
        elif args.detect == "buffer":
            detect_buffer_overflow()
        elif args.detect == "trapdoor":
            detect_trapdoor()
        elif args.detect == "dns":
            detect_dns_poisoning()

    if args.fix:
        if args.fix == "dns":
            fix_dns()

    if args.report:
        generate_report()

if __name__ == "__main__":
    main()
