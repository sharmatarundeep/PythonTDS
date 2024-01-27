myfile = open("/Users/tarundeep/Desktop/python/UDEMY/Basics/Fundamentals/file_operations/file_routers.txt", "r")
print (myfile.mode)
print (myfile.read()) # read whole file
# cursor concept
print (myfile.read(5)) # nothing is printed
#move cursor back to position you want
myfile.seek(0)
print (myfile.read(5)) # now cisco will print
print (myfile.tell()) # to check where is the cursor now
myfile.seek(0)
print (myfile.tell())
# read line one by one and one at a time
myfile.seek(0)
print (myfile.readline()) # first line which is cisco
print (myfile.readline()) # second line which is juniper

# read all lines in one go
myfile.seek(0)
print (myfile.readlines()) # return a list with each line as an element of the list



