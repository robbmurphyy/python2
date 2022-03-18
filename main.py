#Author: Robert Murphy
#Class: Python 307
#Midterm - main file
#date 3/18/22

import psutil
import find_currrent_network_Midterm

if __name__ == '__main__':
    print("Run this on WINDOWS!!!!!!\n")
    if psutil.WINDOWS != True:
        print("This program can only be run on WINDOWS!\n")
    else:
        ip = find_currrent_network_Midterm.discover_current_ip_and_network()
        print("\nHere are the WI-FI connected devices:")
        find_currrent_network_Midterm.scan_for_connected_hosts(ip)





