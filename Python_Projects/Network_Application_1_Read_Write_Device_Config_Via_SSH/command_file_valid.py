# Make sure that the file with commands is present in local file system
import sys
import os.path

def command_file_valid():
    cmd_file = input("Enter command file path and name")

    #check if file exist 
    if os.path.isfile(cmd_file) == True:
        print ("Command file exist")
        return cmd_file
    else:
        print ("Command file doesn't exist, please enter valid path and file name for the file")
        sys.exit() # exit the program

#command_file_valid() # just for testing

