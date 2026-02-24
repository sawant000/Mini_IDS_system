import time
import re
from collections import defaultdict

FAILED_THRESHOLD = 3

def monitor_logs(file_path):
    print("=" * 60)
    print(" Mini Intrusion Detection System (IDS) ")
    print("=" * 60)
    print("Monitoring started... Press CTRL+C to stop.\n")

    failed_attempts = defaultdict(int)
    file_position = 0

    while True:
        with open(file_path, "r", encoding="utf-8") as file:
            file.seek(file_position)
            new_lines = file.readlines()
            file_position = file.tell()

        for line in new_lines:
            match = re.search(r"(\d+\.\d+\.\d+\.\d+)", line)
            if match:
                ip = match.group(1)

                if "Failed login" in line:
                    failed_attempts[ip] += 1

                    if failed_attempts[ip] >= FAILED_THRESHOLD:
                        print(f"[ALERT] Possible Brute Force Attack from {ip}")

                if "Successful login" in line and failed_attempts[ip] >= FAILED_THRESHOLD:
                    print(f"[CRITICAL] Account Compromise Risk from {ip}")

        time.sleep(3)

def main():
    file_path = "attack_log.txt"
    monitor_logs(file_path)

if __name__ == "__main__":
    main()