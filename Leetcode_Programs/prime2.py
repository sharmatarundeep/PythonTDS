# Find prime number between range of integers

n1= raw_input("enter first number")
n2= raw_input("enter second number")
n11= int(n1)
n22= int(n2)

for i in range(n11,n22+1):
  count = 2
  for j in range(2,i):
    if i%j==0:
      print str(i)+" is not a prime number"
      break
    else:
      count=count+1
  if count==i:
    print str(i)+" is a prime number"


