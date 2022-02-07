#Author: Robert Murphy
#Class: Python 307
#Assignment project 1, psutil
#date 2/3/22

import psutil
import sys
import getopt
import platform
import subprocess
import os
import signal
import time

#----------------------------------------------

def whatOS(): #tells you what os you are using
    if psutil.LINUX == True:
        print("Your current operating system is Linux.")
        print("Properties:", platform.uname())
    elif psutil.WINDOWS == True:
        print("Your current operating system is Windows.")
        print("Properties:", platform.uname())
    elif psutil.MACOS == True:
        print("Your current operating system is Linux.")
        print("Properties:", platform.uname())

def getUsers(): #displays all users
    users = psutil.users()
    for user in users:
        print(user.name, "\n", "\tHostname:", user.host, "\n", "\tCreation (seconds since epoch):", user.started)
        if psutil.LINUX == True:
            print("\n\tTerminal:", user.terminal, "\n", "\tPID of login process:", user.pid)

def getProcesses(): #displays 10 running processes
    counter = 0
    print("Here are 10 processes running on the system")
    for proc in psutil.process_iter(['pid', 'name', 'username']):
        print(proc.info)
        counter += 1
        if counter == 10:
            break

def pythonHunter(): #creates python instance, finds its pid, and kills it
    process1 = subprocess.Popen(["python3"]).pid
    print("Hunting for python process")
    time.sleep(2)
    for proc in psutil.process_iter(['name', 'pid']):
        if process1 == proc.info['pid']:
            print("\nfound python at PID", {proc.info['pid']}, "\nprepare to die...")
            os.kill(int(proc.info['pid']), signal.SIGTERM)
            time.sleep(2)
            print("bye python :)")
            break


#-----------------------------------------------
argList = sys.argv[1:]
options = "wuph"
longOptions = ["os", "users", "processes", "hunter"]
try:
    arguments, values = getopt.getopt(argList, options, longOptions)

    for currentArg, currentVal in arguments:
        if currentArg in ("-w", "--os"):
            whatOS()
        elif currentArg in ("-u", "--users"):
            getUsers()
        elif currentArg in ("-p", "--processes"):
            getProcesses()
        elif currentArg in ("-h", "--hunter"):
            pythonHunter()
except getopt.error as err:
    print("Wrong args. Enter -w or --os for whatOS() #4")
    print("-u or --users for getUsers() #5")
    print("-p or --processes for getProcesses() #6")
    print("-h or --hunter for pythonHunter) #7 & 8")