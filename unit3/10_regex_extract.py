import re
import os

log = """2024-01-15 10:30:45 INFO Login: deep@mu.edu
2024-01-15 10:31:22 ERROR Failed: 192.168.1.1
2024-01-15 10:32:10 INFO Login: goat@mu.edu"""

with open("log.txt", "w") as f:
    f.write(log)

with open("log.txt") as f:
    content = f.read()

print("Emails:", re.findall(r"[\w.]+@[\w.]+\.\w+", content))
print("IPs:", re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", content))
print("Dates:", re.findall(r"\d{4}-\d{2}-\d{2}", content))
print("Times:", re.findall(r"\d{2}:\d{2}:\d{2}", content))
print("Levels:", re.findall(r"INFO|ERROR|WARN", content))

for lvl, msg in re.findall(r"(INFO|ERROR|WARN)\s+(.+)", content):
    print(f"[{lvl}] {msg}")

os.remove("log.txt")