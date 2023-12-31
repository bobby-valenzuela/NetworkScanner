#!/usr/bin/env python

import os
import scapy.all as scapy
import argparse
# Create the parser
parser = argparse.ArgumentParser()
# Add an argument
parser.add_argument('-t', '--target', type=str, required=False)
# Parse the argument
args = parser.parse_args()
# Print "Hello" + the user input argument

debug = False

if debug : print("Running...")

def scan_w_scapy(ip):
    scapy.arping(ip)

def scan(ip):


    # ip - (192.168.1.1/24) ideally would be a cidr addr so  we can check all hosts on a network

    ### ARP: Build arp packet
    # Build arp packet + send to destination
    arp_request = scapy.ARP(pdst=ip)    # pdst - packet destination

    # Arp summary: "who has <ip> says <my ip/system sending arp>"
    if debug : print(arp_request.summary())  
    
    # Deatils of arp request
    if debug : arp_request.show()



    ### ETHERNET: Build ethernet frame
    # Build ethernet frame destined for broadcast address
    broadcast_frame = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")

    # Print broadcast summary
    if debug : print(broadcast_frame.summary())    

    # Deatils of eth frame frame
    if debug : broadcast_frame.show()
    

    ### BUILD FINAL PAKCET: Arp packet + Ether frame
    arp_request_broadcast = broadcast_frame/arp_request # scapy syntax to combine
    if debug : arp_request_broadcast.show()

    
    # SRP: SEND PACKET + RECEIVE RESPONSE 
    # scapy.srp() - is a send/request function that allows us to use our own cutom Ethernet frame unlike scapy.sr()
    answered_list = scapy.srp(arp_request_broadcast, timeout = 1, verbose = debug)[0]
    if debug : print(answered_list.summary())

    # FORMAT FINDINGS
    print('\nIP\t\t\tMAC Adddres\n----------------------------------------')
    for  element in answered_list:
        print(f"{element[1].psrc}\t\t{element[1].hwsrc}")

    print("")

    # ###[ Ethernet ]### 
    #   dst       = ff:ff:ff:ff:ff:ff           <- destination_mac: broadcast mac - forwarded to every device on network
    #   src       = 00:15:5d:56:34:04           <- senders mac (me)
    #   type      = ARP                         <- ARP - see ARP packet for details of arp request (below)
    # ###[ ARP ]### 
    #      hwtype    = Ethernet (10Mb)
    #      ptype     = IPv4
    #      hwlen     = None
    #      plen      = None
    #      op        = who-has                  <- operation: arp query
    #      hwsrc     = 00:15:5d:56:34:04        <- senders mac (me)
    #      psrc      = 172.25.247.139           <- senders ip (me)
    #      hwdst     = 00:00:00:00:00:00        
    #      pdst      = Net("172.25.247.1/24")   <- packet desintation: every ip in subnet (Ethernet frame makes sure the this request goes to broadcast MAC)



    # === DEBUG ===
    # List object fields to set
    # scapy.ls(scapy.ARP())
    


# MAIN
if __name__ == '__main__':


    ip = ""
    print(f"ARGS: {args}\n")
    if 'IP_RANGE' in os.environ :
        ip = os.environ['IP_RANGE']
    elif not args.target == "":
        ip = args.target  
    else:
        ip = '172.17.0.1/24'
    
    print(f"Using: {ip}")
    scan(ip)


# import subprocess
# response = subprocess.run( ["ip", "a"], shell=True, capture_output=True, text=True ) 

# print(f"STDOUT:{response.stdout}")