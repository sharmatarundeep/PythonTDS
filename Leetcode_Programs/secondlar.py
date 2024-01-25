l=[2,1,1,3,4,6,5,10,11,49,54,34,6,50,50,54]
print l
noe=len(l)
l.sort()
print l
for i in range(0,noe):
  if l[noe-i-1] != l[noe-i-2]:
    print "second largest element is " + str(l[noe-i-2])
    exit()
    
