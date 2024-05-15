#!/usr/bin/env python3

"""Simple pinging your site"""

import os

address = "sstmk.ru"

response = os.popen(f"ping {address} ").read()

if ("Request timed out." or "unreachable") in response:
    print(f"Ping Unsuccessful, Host is DOWN.")
else:
    print(f"IP-address of {address} is  - {response[28:41]} - Ping Successful, Host is UP!")
