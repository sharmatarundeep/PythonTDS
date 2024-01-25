'''steps
1. open the file in read mode
2. read all lines to get a list of all lines as elements
3. iterate the list and print the elements start with A'''

myfile = open("/Users/tarundeep/Desktop/python/UDEMY/Basics/Fundamentals/file_operations/file_routers.txt","r")
myfile.seek(0)
for x in myfile.readlines():
    if x[0] == "A":
        print(x)