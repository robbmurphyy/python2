#Author: Robert Murphy
#Class: Python 307
#Midterm - secondary file to find the current network and connected hosts
#date 3/18/22

import scapy.all as scapy
import re

#seperates IP into a list based off each octet and cuts off the last octet
def extract_three_octet_IP(ipStr):
    l = re.split('(.*)\.(.*)\.(.*)\.(.*)', ipStr)
    return l[1:-2]

#discovers the network/ip the system is on and returns a IP string
def discover_current_ip_and_network():
    ipaddy = scapy.get_if_addr(scapy.conf.iface)
    print("Your IP address is:", ipaddy)
    three_oct_ip = ""
    cut_ip = extract_three_octet_IP(ipaddy)

    for element in cut_ip: #turns list into string
        three_oct_ip += element
        three_oct_ip += "."
    three_oct_ip += "0" #adds 4th octet as a 0

    #adds the cidr notation
    IP_to_scan = three_oct_ip + "/24"
    print("Your system has the netmask with the network address of", three_oct_ip, "and Output IP of", ipaddy)
    print(scapy.conf.route)
    return IP_to_scan

#this creates an ARP request that is broadcasted to the system's network and displays responses
def scan_for_connected_hosts(ip):
    arp_packet = scapy.ARP(pdst=ip)
    l2_broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    broadcast_and_arp = l2_broadcast / arp_packet
    answered_list = scapy.srp(broadcast_and_arp, timeout=2, verbose=False)[0]
    results = []
    for i in range(0, len(answered_list)):
        client_dict = {"ip": answered_list[i][1].psrc, "mac": answered_list[i][1].hwsrc}
        results.append(client_dict)
    for k in results:
        print(k)


