import os
import sys

import requests

URL = "https://api.ipify.org/?format=json"

PROXY1 = os.getenv("PROXY1")
PROXY2 = os.getenv("PROXY2")
EXPECTED1 = os.getenv("EXPECTED1")
EXPECTED2 = os.getenv("EXPECTED2")

if not PROXY1 or not PROXY2 or not EXPECTED1 or not EXPECTED2:
    print("Please set needed ENV vars. E.g. start like this:")
    print("PROXY1=192.168.1.200:5001 PROXY2=192.168.6.1:4002 EXPECTED1=123.123.123.123 EXPECTED2=124.124.124.124 python main.py")
    sys.exit()


if __name__ == "__main__":
    proxy = f"http://{PROXY1}"
    print(f"Testing proxy 1: with proxy_addr: {proxy}")
    response = requests.get(URL, proxies={"http": proxy, "https": proxy}).json()
    assert response["ip"] == EXPECTED1, response["ip"]
    print("Proxy 1: OK")

    proxy = f"http://{PROXY2}"
    print(f"Testing proxy 2: with proxy_addr: {proxy}")
    response = requests.get(URL, proxies={"http": proxy, "https": proxy}).json()
    assert response["ip"] == EXPECTED2, response["ip"]
    print("Proxy 2: OK")
