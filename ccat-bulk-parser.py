#! /usr/bin/env python3

import os
import sys

dir = sys.argv[1]

for root,dir,files in os.walk(dir):
    for name in files:
        if "html" in name:
            fullpath = os.path.join(root,name)
            with open(fullpath) as f:
                content = f.readlines()
                ssh, arp, dhcp_snoop, dhcp_guard, des_guard,source_guard,arp_proxy,portfast,loopguard,bpdu,mode,dtp, unused,aaa,console = False,False,False,False,False,False,False,False,False,False,False,False,False,False,False
                for line in content:
                    if "SSH version" in line and "color: green" not in line:
                        ssh = True
                    if "ARP inspection" in line and "color: green" not in line:
                        arp = True
                    if "DHCP snooping" in line and "color: green" not in line:
                        dhcp_snoop = True
                    if "destination guard" in line and "color: green" not in line:
                        des_guard = True
                    if "DHCP guard" in line and "color: green" not in line:
                        dhcp_guard = True
                    if "Source Guard" in line and "color: green" not in line:
                        source_guard = True
                    if "ARP-proxy" in line and "color: green" not in line:
                        arp_proxy = True
                    if "Portfast" in line and "color: green" not in line:
                        portfast = True
                    if "Loopguard" in line and "color: green" not in line:
                        loopguard = True
                    if "Bpduguard" in line and "color: green" not in line:
                        bpdu = True
                # F-02 
                #print(fullpath + ":" + str(ssh) + ":" + str(arp) + ":" + str(dhcp_snoop) + ":" + str(dhcp_guard) + ":" + str(des_guard) + ":" + str(source_guard) + ":" + str(arp_proxy) + ":" + str(portfast) + ":" + str(loopguard) + ":" + str(bpdu))
                    if "- mode" in line and "color: green" not in line:
                        mode = True
                        
                    if "Dynamic Trunking Protocol(DTP)" in line and "color: green" not in line:
                        dtp = True
                    if "Unused Interface" in line and "color: green" not in line:
                        unused = True
                # F-04
                print(fullpath + ":" + str(mode) + ":" + str(dtp) + ":" + str(unused))
                # F-06 AAA misconfigured no Console auth and case-insensitive passwords 
                    # if 'list "aaatacacs" method' in line and "color: green" not in line:
                    #     aaa = True
                    # if 'list "console" method' in line and "color: green" not in line:
                    #     console = True
                # print(fullpath + ":" + str(aaa) + ":" + str(console)) 
