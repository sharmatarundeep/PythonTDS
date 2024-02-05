# Check the IP address file is present in local file system, read its context and return IP address as a list
import sys
import os.path

def ip_file_valid():
    ip_file = input("Enter IP address file path and name")

    #check if file exist 
    if os.path.isfile(ip_file) == True:
        print ("IP address file exist")
    else:
        print ("IP address file doesn't exist, please enter valid path and file name for the file")
        sys.exit() # exit the program
    
    # Open the file in read mode and read all the IP adress and store as a list
    selected_ip_file = open(ip_file,"r")

    # Read all the ip addresses and store in the list
    selected_ip_file.seek(0) # bring cursor to 0 just to be sure
    ip_list = selected_ip_file.readlines() 
    
    return ip_list # This is the list of all the IP address specific in the ip.txt file




