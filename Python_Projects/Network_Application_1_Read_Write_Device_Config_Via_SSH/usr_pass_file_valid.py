# Make sure that the file containing user name and password is present in local file system or not
import sys
import os.path

def usr_pass_valid():
    usr_file = input("Enter Username and Password file path and name")

    #check if file exist 
    if os.path.isfile(usr_file) == True:
        print ("Username and Password file exist")
        return usr_file
    else:
        print ("Username and Password file doesn't exist, please enter valid path and file name for the file")
        sys.exit() # exit the program


#usr_pass_valid() # just for testing

