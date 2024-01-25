import os
# function gives the name of the operating system dependent module
print (os.name) # posix 

# print current working directory
print (os.getcwd()) # /Users/tarundeep/Desktop/python

# rename a file in python
import os
f1=open("old.txt","w")#create a file 
f1.close()
f2="old.txt"
os.rename(f2,"new.txt")

#Return information identifying the current operating system.
print (os.uname())     

#Return a list of the files in the directory in given path.
print (os.listdir("/Users/tarundeep/Desktop/python"))
print (os.listdir("."))

#Create a directory named tarun.
os.mkdir("tarun")    

#Rename the file or directory src to dst.
#os.rename(src, dst)
os.rename("tarun", "tarunnew")  


