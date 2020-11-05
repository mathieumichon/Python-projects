#!/usr/bin/python3

# === HEADER ===
# serial: 20/10/2020|02
# description: Simple code using scapy that scans on a given address range and specified ports
# project: None
# members: 
# - MICHON Mathieu (michon@et.intechinfo.fr)
# ==============

from scapy.all import *
from sys import *
from json import *
from re import *

def show_syntax():
    print("""- invalid syntax -
    syntax: args [address-range] [ports]
    example:
        - use ',' to specify each port
            scan_machines.py 192.0.0.10-20 22,80,443
        - use '-' to set a range of ports
            scan_machines.py 192.0.0.10-20 22-443
    """)

try:
    # check the syntax of the arguments
    if sys.argv[1] and sys.argv[2] and (((',' in sys.argv[2] or not ',' in sys.argv[2]) and not '-' in sys.argv[2]) or '-' in sys.argv[2] and not ',' in sys.argv[2]):
        # get the address range given as argument
        add_range = sys.argv[1]

        # we parse the ports given as argument
        # [ specified ports ]
        if ',' in sys.argv[2] or not '-' in sys.argv[2] and not ',' in sys.argv[2]:
            arg_ports = re.split(',', sys.argv[2])
            for index in range(0, len(arg_ports)):
                arg_ports[index] = int(arg_ports[index])
        # [ from port x to port y ]
        else:
            arg_ports = re.split('-', sys.argv[2])
            # only 2 elements are needed (start & end of the range)
            del arg_ports[2:]
            for index in range(0, len(arg_ports)):
                arg_ports[index] = int(arg_ports[index])
            arg_ports = tuple(arg_ports)

        print('Scanning addresses..')
        # we buid the PING packet & send it to each addresses
        rep,non_rep = sr(IP(dst=add_range) / ICMP(), timeout=0.5)
        machines_tab = {}
        for elem in rep:
            # if the address answers, we store it
            if elem[1].type == 0:
                machines_tab[elem[1].src] = {'ports' : []}

        # for each address
        for machine in machines_tab:
            # we send a packet to each port within the range given
            mon_paquet = IP(dst=machine) / TCP(sport=12345, dport=arg_ports, flags='S')
            rep,non_rep = sr(mon_paquet)
            for emis,recu in rep:
                # if we get an answer we store the port as opened
                if recu[1].flags == 18: # 18 <=> SYN+ACK
                    machines_tab[machine]['ports'].append(recu[1].sport)

        # we print each address and its opened ports
        print('Opened ports')
        for machine in machines_tab:
            sys.stdout.write('[' + machine + "]")
            if machines_tab[machine]['ports']:
                print('')
                for port in machines_tab[machine]['ports']:
                    print('  -' + str(port))
            else:
                print(" None")
    else:
        show_syntax()
except IndexError:
    show_syntax()
