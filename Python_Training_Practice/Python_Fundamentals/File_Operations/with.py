# if you want auto close of file use "with"
with open("/Users/tarundeep/Desktop/python/UDEMY/Basics/Fundamentals/file_operations/newfile_created_by_w_mode.txt","a+") as myfile:
    print(myfile.closed) #false
    myfile.write("Brocade\n")
    myfile.seek(0)
    print(myfile.read())
print (myfile.closed) # True as it auto closed