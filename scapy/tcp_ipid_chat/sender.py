#!/usr/bin/python3

# === HEADER ===
# serial: 20/10/2020|01
# description: Program that instances a chat to send messages through packets IPID
# project: TCP_chat
# members: 
# - MICHON Mathieu (michon@et.intechinfo.fr)
# ==============

from scapy.all import *

# we set a fixed unused IP (could be a used one but since we're looking for discretion, it would not be clever from us)
target_address      = "213.213.213.213"
previous_id         = 0

# sends the message
def send_msg(msg):
    global target_address
    global previous_id
    # for each character in the message..
    for index in range(len(list(msg))):
        # we check if it's the last character of the message
        msg_state   = "0" if index == (len(msg) - 1) else "1"
        # we set the IPID equals to : (the sum of previous IPID + ASCII code of the character) + the msg state [0 = last char]
        ip_id       = str(previous_id + ord(msg[index])) + msg_state
        # the previous_id becomes now what is the current IPID
        previous_id = int(ip_id[:-1])
        # we send the packet (the "dport" argument isn't very important)
        sr(IP(dst=target_address, id=int(ip_id), ttl=1) / TCP(dport=[4321]), verbose=False)
    # once all the characters are sent, we reset the previous_id value
    previous_id = 0

# we start the chat instance
while True:
    user_msg = input("Me: ")
    if user_msg == "/disconnect": 
        # closes the instance
        break
    else:
        send_msg(user_msg)
