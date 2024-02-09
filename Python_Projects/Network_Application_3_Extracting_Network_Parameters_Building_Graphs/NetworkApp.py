# First we will connect to Arista switch using SSH
# A few variables
smm353_ip = "172.30.190.31"
username = "root"
password = "arastra"
command = "show processes top once"

import sys
import subprocess
import paramiko # used for SSH and networking remote connectivity
import time
import re
import os.path 

# check ip reachability
def ip_reach(ip):
    ip = ip.rstrip("\n")
    ping_reply = subprocess.call('ping %s -c 2' % ip, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, shell=True)
    if ping_reply == 0: # 0 is for echo reply 
        print ("Device is reachable: ", ip)
    else:
        print ("Device is not reachable: ", ip)
        sys.exit()
#ip_reach (smm353_ip) # just to test if ip is reachable or not

# ssh connection and send basic commands 
def ssh_connection(ip):
    # Login to device
    session = paramiko.SSHClient() # Create new SSH client

    #For testing purposes, this allows auto-accepting unknown host keys. Donot use in production
    session.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    #Connect to device using username and password
    session.connect(ip.rstrip("\n"), username=username, password=password)

    # start an interactive shell session on the router
    connection = session.invoke_shell()

    # send some basic COMMON commands 
    connection.send("FastCli" + "\n")
    time.sleep(1)
    connection.send("enable" + "\n")
    time.sleep(1)
    connection.send("config term" + "\n")
    time.sleep(1)
    connection.send(command.rstrip("\n") + "\n") 
    time.sleep(1)

    #Capturing command output to check any syntax errors
    router_output = connection.recv(65535) # 65535 is max limit of receving data
    #print (router_output)

    # Extract CPU utilization value and store in a text file
    cpu = re.search(b"%Cpu\(s\):(\s)+(.+?)(\s)*us,", router_output) # b is for byte string value
    #print (cpu)
    utilization = cpu.group(2).decode("utf-8") #Extracting the second group, which matches the actual value of the CPU utilization and decoding to the UTF-8 format from the binary data type
    #print (utilization) # 1.6

    # Now lets append the CPU value to the text file with a next line character at the end
    with open("/Users/tarundeep/Desktop/Python_TDS/Python_Projects/Network_Application_3_Extracting_Network_Parameters_Building_Graphs/cpu.txt", "a") as f:
        f.write(utilization + "\n")
        print ("Appended the text file with CPU utilization")

    # At the end closing the SSH connection
    session.close()

# Now we would like to call the ssh_connection function every 10 seconds in a loop to get real time data every 10 seconds
while True: # infine loop until interupted 
    ip_reach(smm353_ip) # first check ip is reachable 
    ssh_connection (smm353_ip) # Now SSH , run command, extract CPU value, append to the text file
    time.sleep(10)

    

    
