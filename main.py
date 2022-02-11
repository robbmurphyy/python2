#Author: Robert Murphy
#Class: Python 307
#Assignment project 3 psutil
#date 2/11/22

import psutil
from psutil._common import bytes2human


#----------------------------------------------
def showDisk():
    try:
        for parts in psutil.disk_partitions(all):
            usage = psutil.disk_usage(parts.mountpoint)
            print("Partition:", parts.device)
            print("Total space in GB:", bytes2human(usage.total))
            print("Free space in GB:", bytes2human(usage.free))
            print("Total space used in GB:", bytes2human(usage.used))
            print("Percent used:", usage.percent)
            print("---------------------------------------------")
            #print(parts.mountpoint)

    except OSError:
        print("Issue with the path")

def showMemory():
    print("Here is information about your system's memory usage.")
    mem = psutil.virtual_memory()
    print("Total memory:", bytes2human(mem.total))
    #print("Available memory:", bytes2human(mem.available))
    print("Used memory:", bytes2human(mem.used))
    print("Free memory:", bytes2human(mem.free))
    print("--------------------------------")

def newPartition():


#--------------------------------------------

if __name__ == '__main__':
    print("\n!!!This program is meant to run on Windows 10!!!\n")

    print("Please enter the number that corresponds with what you want to do:")
    choice = input("1:\tDisplay all disks and current usage\n2:\tDisplay all memory statistics\n3:\tCreate a new partition, mount it, and then delete it\n")

    try:
        user_choice = int(choice) # handle this error
        if user_choice != 1 and user_choice != 2 and user_choice != 3:
            user_choice = int(input("You did not enter 1,2, or 3. Please enter one of them."))

        if user_choice == 1:
            showDisk()
        elif user_choice == 2:
            showMemory()
        # elif user_choice == 3:
        #     newPartition()

    except ValueError:
        print("Only enter a number for your choice of method")


