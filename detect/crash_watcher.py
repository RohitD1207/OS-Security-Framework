import subprocess
import time
import re
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from utils import log_alert

LOG_FILE = "crash_log.txt"
CRASH_PATTERN = re.compile(r"segfault|Segmentation fault|RIP:")

def check_dmesg():
    try:
        output = subprocess.check_output(["dmesg", "--ctime", "--color=never"], text=True)
        return output.splitlines()
    except subprocess.CalledProcessError as e:
        print(f"Error reading dmesg: {e}")
        return []

def watch_crashes():
    print("🚨 Crash Watcher: Monitoring for segmentation faults...")
    seen_lines = set()

    while True:
        logs = check_dmesg()
        new_crashes = []

        for line in logs[-30:]:
            if CRASH_PATTERN.search(line) and line not in seen_lines:
                new_crashes.append(line)
                seen_lines.add(line)

        if new_crashes:
            print("🔥 Crash detected:")
            for crash in new_crashes:
                print("   ->", crash)
                with open(LOG_FILE, "a") as f:
                    f.write(crash + "\n")
                log_alert("Segmentation fault detected: " + crash)

        time.sleep(3)

if __name__ == "__main__":
    watch_crashes()
