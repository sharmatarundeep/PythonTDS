l=[3,2,1,4,5,8,7,1]
print l
noe=len(l)
print "number of element in list are:" + str(noe)

for i in range(0,noe):
  for j in range(i+1,noe):
    temp=0
    if l[i]>l[j]:
      temp=l[i]
      l[i]=l[j]
      l[j]=temp

print "sorted list is "
print l


