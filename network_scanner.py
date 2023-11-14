#!/usr/bin/env python

import os
import scapy.all as scapy

print("Running...")

def scan(ip):
    scapy.arping(ip, iface="eth0")

ip_range = os.environ['IP_RANGE']
scan(ip_range)


# import subprocess
# response = subprocess.run( ["ip", "a"], shell=True, capture_output=True, text=True ) 

# print(f"STDOUT:{response.stdout}")