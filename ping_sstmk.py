#!/usr/bin/env python3

"""Simple pinging your site"""

import os

address = "sstmk.ru"

response = os.popen(f"ping {address} ").read()
if response:
    print(f"IP-address of {address} is  - {response[28:41]} - Ping Successful, Host is UP!")
else:
    print(f"Ping Unsuccessful, Host is DOWN.")
