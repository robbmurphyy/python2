#Author: Robert Murphy
#Class: Python 307
#Assignment 4 socket
#date 2/18/22

import socket
from datetime import datetime

#This function determines what the host will be to scan
def host_to_scan():
    user_ip = input("To enter a specific IP enter 'Y', otherwise enter anything else and it will scan localhost by default: ")
    ip = ""
    if user_ip.upper() == 'Y':
        ip = input("Please enter the IP address you want to scan: ")
        print(ip, "will be scanned")
    else:
        print("The localhost 127.0.0.1 will be scanned")
        ip = "localhost"
    return ip

#Creates a socket and connects to the specified ip then scans 65535 ports to see what's open
def port_scanner():
    ip = host_to_scan()
    print("Starting scan at", str(datetime.now()), "...might take a while")
    try:
        for i in range(1, 65535):
            my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            connection = my_socket.connect_ex((ip,i))
            if connection == 0:
                print("Port", i, "is open")
            my_socket.close()
    except socket.timeout:
        print("connection timed out")
    except socket.gaierror:
        print("host could not be resolved")
    except socket.error:
        print("The server isn't responding")
    except KeyboardInterrupt:
        print("Keyboard interrupt!")

if __name__ == '__main__':
    port_scanner()







