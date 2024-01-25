#extract something from a string
str1="Eth1 10.1.1.1/24 UP"
print (str1[5:16]) #start index5 to index16
print (str1[:]) #whole staring
print (str1[:16]) #until index 16
print (str1[5:]) #start from index 5 to end
print (str1[-2:-1]) # U = start at -2 to -1 but -1 will not be included
print (str1[-2:]) # UP = start at -2 till end
print (str1[-5:]) # last 5 character
print (str1[:-5]) # skip last 5 charac
print (str1[::2]) #step - every 2 char will be printed
print (str1[::-1]) #reverse string
