#Author: Robert Murphy
#Class: Python 307
#Assignment 3 psutil
#date 2/11/22

import psutil
from psutil._common import bytes2human
import time

def show_disk():
    try:
        for parts in psutil.disk_partitions(all):
            usage = psutil.disk_usage(parts.mountpoint)
            print("Partition mounted on:", parts.device)
            print("Total space in GB:", bytes2human(usage.total))   #bytes2human reads in bytes and outputs it in GB
            print("Free space in GB:", bytes2human(usage.free))
            print("Total space used in GB:", bytes2human(usage.used))
            print("Percent used:", usage.percent)
            print("-----------------------------------------")
    except OSError:
        print("Issue with the inputted path")

def show_memory():
    print("Here is information about your system's memory usage.")
    mem = psutil.virtual_memory()
    print("Total memory:", bytes2human(mem.total))
    print("Used memory:", bytes2human(mem.used))
    print("Free memory:", bytes2human(mem.free))
    print("--------------------------------")

def create_new_partition_and_delete_it():
    print("This function will not actually execute the commands I am printing out what I would execute.")
    time.sleep(3)
    print("p = Popen(['diskpart'])")
    print()
    time.sleep(2)
    print("p.communicate(input=b'LIST DISK')")
    print("p.communicate(input=b'SELECT DISK 0')")
    print("p.communicate(input=b'LIST PARTITION')")
    print("p.communicate(input=b'CREATE PARTITION PRIMARY SIZE=1000')") #size is specified in MB
    print("p.communicate(input=b'ASSIGN LETTER=S')")
    print()
    time.sleep(2)
    print("p.communicate(input=b'LIST PARTITION')")
    print("p.communicate(input=b'LIST DISK')")
    print()
    time.sleep(2)
    print("p.communication(input=b'SELECT PARTITION 5')")
    print("p.communicate(input=b'DELETE PARTITION')")
    print("p.communicate(input=b'LIST PARTITION')")
    #https://www.techtarget.com/searchwindowsserver/tip/Using-Diskpart-to-create-extend-or-delete-a-disk-partition
    #https://computingforgeeks.com/how-to-create-disk-partitions-in-windows-using-diskpart-command/


if __name__ == '__main__':
    print("\n!!!This program is meant to run on Windows 10!!!\n")
    print("Please enter the number that corresponds with what you want to do:")
    choice = input("1:\tDisplay all disks and current usage\n2:\tDisplay all memory statistics\n3:\tCreate a new partition, mount it, and then delete it\n")
    try:
        user_choice = int(choice)
        if user_choice != 1 and user_choice != 2 and user_choice != 3:
            user_choice = int(input("You did not enter 1,2, or 3. Please enter one of them."))
        if user_choice == 1:
            show_disk()
        elif user_choice == 2:
            show_memory()
        elif user_choice == 3:
            create_new_partition_and_delete_it()
    except ValueError:
        print("Only enter a number for your choice of method")


