# Purpose of this tool is to create multiple sessions to a device and run a show command to from each session to spike the CPU
import sys
import paramiko # used for SSH and networking remote connectivity
import time
import re
import os.path 
import sys
import threading

#this func will take care of creating multiple threads for SSH to IP
def create_threads(ip, num_thread, func): 
    thread = [] # empty list to store the thread object for later execution 
    for x in range(int(num_thread)):
        th = threading.Thread(target = func, args= (ip,))
        th.start()
        thread.append(th)
        print ("Hello")
    for th in thread:
        th.join()

def ssh_connection(ip):
    # Create SSH connection
    try: # for error handling 
        username = 'admin'
        password = ''
        # Login to device
        session = paramiko.SSHClient() # Create new SSH client
        #For testing purposes, this allows auto-accepting unknown host keys. Do not use in production
        session.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        #Connect to device using username and password
        session.connect(ip, username=username, password=password)
        # start an interactive shell session on the router
        connection = session.invoke_shell()
        
        connection.send("show ip bgp" + "\n")
        time.sleep(3)
        print ("Executing show command")

        #Closing the SSH connection
        session.close()

    except paramiko.AuthenticationException: # to add exception handling for wrong username / password
        print ("Authentication Failed for : ", ip)
        print("Closing program... Bye!")

# Saving the list of IP addresses in a variable 
ip = "172.24.64.31"

# Now call create_thread func to start executing commands on all devices simultaneously
# arguments to be passed are ip add, number of sessions and function to be called for each session
while True: # create and close sessions again and again to keep CPU busy
    create_threads(ip, '20', ssh_connection)
    print ("Creating threads again")

