#!/usr/bin/python3

# === HEADER ===
# serial: 20/10/2020|01
# description: Sniffs packets that have a specific IP dst and then decodes the messages through their IPID
# project: TCP_chat
# members: 
# - MICHON Mathieu (michon@et.intechinfo.fr)
# ==============

from scapy.all  import *
from threading  import *
import re
import uuid

# the target address has to be the same as in the sender.py file
target_address = "host 213.213.213.213"
current_message = ""
previous_id     = 0

# this function is called for each sniffed packet, so for each packet..
def decode_packet(packet):
    global current_message
    global previous_id
    # we get the IPID of the packet
    ip_id       = str(packet.id)
    # we get the current IPID by removing the last character that is equal to the message state [1/0]
    current_id  = int(ip_id[:-1])
    # we get the characters that is equal to the ASCII code we obtained by that substraction
    character   = chr(current_id - previous_id)
    # the previous_id becomes now what is the current IPID
    previous_id = current_id
    # we get the state of the message that indicates if it was the last character of the letter or not
    state       = ip_id[-1]

    # then we add the decoded character to our message under construction
    current_message += character
    # if it was the last character of the message
    if state == "0":
        # === only usefull for the display of our own messages ===
        # we get the local MAC address 
        local_mac_addr   = ':'.join(re.findall('..', '%012x' % uuid.getnode()))
        # we get the src MAC address of the packet
        src_mac_addr     = packet.src
        # we change the color of the output in case it is (or isn't) ours
        addr_color       = '\x1b[92m' if src_mac_addr == local_mac_addr else '\x1b[96m'
        # ===
        # we display the message with the src MAC address
        print(f"[{addr_color}{packet.src}\x1b[0m]: {current_message}")
        # once we finally displayed rhe message, we reset the global values
        current_message = ""
        previous_id = 0

# we start the sniff
sniff(filter=target_address, prn=decode_packet)
