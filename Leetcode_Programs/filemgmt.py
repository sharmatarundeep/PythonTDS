f=open("file.txt","w")
f.write("this is 4th line")
f.close()
f=open("file.txt","r")
print (f.read())
f.close()

