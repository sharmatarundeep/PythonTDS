print "Enter a number for which you want to find the divisor"
num = raw_input()

l =[]
for i in range(1,int(num)+1):  
  if int(num)%i==0:
    l.append(i)
  i=i+1

print l
