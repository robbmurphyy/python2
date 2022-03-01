#Author: Robert Murphy
#Class: Python 307
#Assignment 5 sniffer
#date 2/25/22


from scapy.all import *

#This method performs the sniffing and prints out each packet captured
def sniffer(num):
    cap = sniff(filter='ip', prn=lambda x:x.sprintf("Time: %IP.time%, HostIP: %IP.src%, DestIP: %IP.dst%, Protocol: %IP.proto%, Data: %Raw.load%"), count=num)
    print(cap)

#runs the program and prompts user for desired number of captures
if __name__ == '__main__':
    try:
        print("Welcome to network sniffer")
        number_of_captures = int(input("Enter number of packets you want to capture or type a letter for a default of 10: "))
        sniffer(number_of_captures)
    except ValueError:
        number_of_captures = 10
        print("Doing 10 captures")
        sniffer(number_of_captures)



