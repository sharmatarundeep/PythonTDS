print "Enter a number"
n=raw_input()
print "number entered by the user is " + n
i=2 #This is to star the logic
n1=int(n)
while i<n1:
  if n1 % i == 0:
    print "number is not prime"
    exit()
  else:
    i=i+1
if i==n1:
  print "number " + n + " is prime"  

