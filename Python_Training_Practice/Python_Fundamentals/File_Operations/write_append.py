#try to create a file which doesn't exist
myfile = open("/Users/tarundeep/Desktop/python/UDEMY/Basics/Fundamentals/file_operations/newfile_created_by_w_mode.txt","w")
#write something to new file
myfile.write("I love python!\nDo you?")
myfile.close() # without this write won't work
# lets try reading it
myfile1 = open("/Users/tarundeep/Desktop/python/UDEMY/Basics/Fundamentals/file_operations/newfile_created_by_w_mode.txt","r")
print (myfile1.read())

# open the same file in w mode
myfile = open("/Users/tarundeep/Desktop/python/UDEMY/Basics/Fundamentals/file_operations/newfile_created_by_w_mode.txt","w")
myfile.write("all old date in file is now GONE!!")
myfile.close() # without this write won't work
myfile1.seek(0)
print (myfile1.read()) # all old data is gone

#use writelines method
myfile = open("/Users/tarundeep/Desktop/python/UDEMY/Basics/Fundamentals/file_operations/newfile_created_by_w_mode.txt","w")
myfile.writelines(['cisco\n','arista\n','juniper\n'])
myfile.close()
myfile1.seek(0)
print (myfile1.read())

#append mode
myfile = open("/Users/tarundeep/Desktop/python/UDEMY/Basics/Fundamentals/file_operations/newfile_created_by_w_mode.txt","a")
myfile.write('HP\n') # HP will get appended at the end of the file
myfile.close()
myfile1.seek(0)
print (myfile1.read())

# r+, w+, a+ mode
myfile = open("/Users/tarundeep/Desktop/python/UDEMY/Basics/Fundamentals/file_operations/newfile_created_by_w_mode.txt","a+")
myfile.write('Nokia\n') # Nokia will get appended at the end of the file
myfile.seek(0)
print (myfile.read())
myfile.close()

# to check if file is closed or not
print (myfile.closed) # True

