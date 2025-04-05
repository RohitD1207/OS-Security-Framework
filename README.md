```md
# OS Vulnerability Simulation Framework

This project is a modular Python-based framework designed to simulate and detect common operating system-level security vulnerabilities. It serves as a learning tool for understanding how such vulnerabilities operate and how they can be detected and mitigated in controlled environments.

---

## Features

- **Attack Simulations**  
  Simulates the behavior of several common vulnerabilities:
  - Buffer Overflow
  - HTTP Trapdoor (Hidden Endpoint)
  - DNS Cache Poisoning

- **Detection Tools**  
  Includes detection scripts that analyze system behavior to identify:
  - Crash logs and segmentation faults
  - Suspicious open or hidden HTTP endpoints
  - DNS spoofing based on expected IP resolution

- **Logging & Reporting**  
  - All detected anomalies are logged to `alerts.log`
  - A CLI-based report summarizing threats and suggested fixes

- **Mitigation Support**  
  Includes tools to restore system configurations (e.g., DNS settings) after simulations.

---

## Usage

Run any of the following commands from the root directory.

### Run Attack Simulations

```bash
python3 framework.py --simulate buffer      # Simulate buffer overflow
python3 framework.py --simulate trapdoor    # Start HTTP server with trapdoor
python3 framework.py --simulate dns         # Poison /etc/hosts DNS entry
```

### Run Detection Tools

```bash
python3 framework.py --detect all           # Run all detection modules
python3 framework.py --detect trapdoor      # Detect hidden HTTP endpoints
python3 framework.py --detect buffer        # Detect crashes
python3 framework.py --detect dns           # Check for DNS spoofing
```

### Fix or Clean Up

```bash
python3 framework.py --fix dns              # Restore /etc/hosts to original state
```

### View Threat Summary

```bash
python3 framework.py --report               # Summary of threats and solutions
```

---

## Project Structure

```
.
├── framework.py               # Main CLI controller
├── simulate/                  # Simulation modules
│   ├── buffer_overflow.c
│   └── http_trapdoor.py
├── detect/                    # Detection modules
│   ├── crash_watcher.py
│   ├── dns_checker.py
│   ├── dns_toggle.py
│   └── trapdoor_scanner.py
├── alerts.log                 # Logs for detected threats
└── README.md
```

---

## Disclaimer

This project is strictly intended for **educational use in secure, sandboxed environments**.  
Running these tools on production systems or unauthorized machines may violate institutional or legal policies.

---

## Author

Submitted by: *Rohit Dharmavaram*  
```