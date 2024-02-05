# Check the command  file is present in local file system
import sys
import os.path

def command_file_valid():
    usr_file = input("Enter Username and Password file path and name")

    #check if file exist 
    if os.path.isfile(usr_file) == True:
        print ("Command file exist")
    else:
        print ("Command file doesn't exist, please enter valid path and file name for the file")
        sys.exit() # exit the program

command_file_valid() # just for testing

