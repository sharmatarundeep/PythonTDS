l=[3,2,1,4,5,8,7,1]
print l
l1=[]
for i in range(0,len(l)):
  l1.append(min(l))
  l.remove(min(l))
print l1
