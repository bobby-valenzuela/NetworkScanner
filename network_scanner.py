#!/usr/bin/env python

import scapy.all as scapy

print("Running...")

def scan(ip):
    scapy.arping(ip, iface="eth0")

ip_range = '172.17.0.0/16' # default docker network
scan(ip_range)


# import subprocess
# response = subprocess.run( ["ip", "a"], shell=True, capture_output=True, text=True ) 

# print(f"STDOUT:{response.stdout}")