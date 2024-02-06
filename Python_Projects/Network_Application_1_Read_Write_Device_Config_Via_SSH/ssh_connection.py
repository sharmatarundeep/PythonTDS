# Objective of this python module is to create SSH connection with the devices and send the specified commands
import paramiko # used for SSH and networking remote connectivity
import time
import re
import os.path 
import sys
#import usr_pass_file_valid
#import command_file_valid

# First lets try to get file path of username/password file and the command file
# Later we will open the 2 files in read mode to get usr/pwd info to remote SSH and send configs to the devices
# So we will use the functions from "command_file_valid.py" and "usr_pass_file_valid.py"
#usr_file = usr_pass_file_valid.usr_pass_valid()
#cmd_file = command_file_valid.command_file_valid()

# Temporary to test the functionality of this module
usr_file = '/Users/tarundeep/Desktop/Python_TDS/Python_Projects/Network_Application_1_Read_Write_Device_Config_Via_SSH/usr_pass.txt'
cmd_file = '/Users/tarundeep/Desktop/Python_TDS/Python_Projects/Network_Application_1_Read_Write_Device_Config_Via_SSH/command.txt'

# Now lets establish the SSH connection
def ssh_connection(ip):
    global usr_file # Bring global varaibles to local namespace of this function
    global cmd_file # Bring global varaibles to local namespace of this function

    # Create SSH connection
    try: # for error handling 
        selected_user_file = open(usr_file,"r") # open the user/pwd file in read mode
        selected_user_file.seek(0) # bring the cursor to beginning
        # read the username by splitting the line to get a list which has first element as username and second element as password
        usr_pass_list = selected_user_file.readlines()[0].split(',') # readlines wil return ['root,arastra'] so to make it ['root', 'arastra'] we need to split
        username = usr_pass_list[0]
        password = usr_pass_list[1].rstrip("\n")
        #print(username) # root - just to test
        #print(password) # arastra - just to test

        # Login to device
        session = paramiko.SSHClient() # Create new SSH client

        #For testing purposes, this allows auto-accepting unknown host keys. Donot use in production
        #session.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        #Connect to device using username and password
        session.connect(ip.rstrip("\n"), username=username, password=password)

        # start an interactive shell session on the router
        connection = session.invoke_shell()

        # send some basic COMMON commands 
        connection.send("FastCli" + "\n")
        time.sleep(1)
        connection.send("enable" + "\n")
        time.sleep(1)

        # Open command file for reading the commands 
        selected_cmd_file = open(cmd_file,"r") # open cmd_file in read mode
        selected_cmd_file.seek(0) # bring the cursor to beginning
        for each_line in selected_cmd_file.readlines(): # ['config terminal\n', 'hostname Tarun\n', 'show ip interface br']
            connection.send(each_line.rstrip("\n") + "\n") # send all the commands from the file
            time.sleep(1)

        # close the user file
        selected_user_file.close()
        # close the command file
        selected_cmd_file.close()

        #Capturing command output to check any syntax errors
        router_output = connection.recv(65535) # 65535 is max limit of receving data
        # print (str(router_output) + "\n")
        if re.search(b"% Invalid input", router_output):
            print("There was at least one syntax error on device : ", ip)
        else:
            print("All command executed on device : ", ip)

        #Closing the SSH connection
        session.close()

    except paramiko.AuthenticationException: # to add exception handling for wrong username / password
        print ("Authentication Failed for : ", ip)
        print("Closing program... Bye!")

ssh_connection("172.30.190.25") # for testing this modules functionality 

