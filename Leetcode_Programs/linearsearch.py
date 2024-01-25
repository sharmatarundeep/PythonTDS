l=[1,3,2,99,100,23,5,6,7,9,10,11,12,13]
print l
n=raw_input("Enter the number you want to search:")
noe=len(l)
count=0
for i in range(0,noe):
  if int(n) == l[i]:
    print "Number " + n + " is present at index " + str(i)
    exit()
  else:
     count=count+1
if count == noe:
  print "number entered is not present in the list"

