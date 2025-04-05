import datetime

def log_alert(message):
    timestamp = datetime.datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
    with open("alerts.log", "a") as f:
        f.write(f"{timestamp} {message}\n")