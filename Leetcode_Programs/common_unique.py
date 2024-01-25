l1=[1,2,3,3,4,5]
l2=[3,4,5,6,7,8]
lcomm=[]
luni=[]

for i in l1:
  if i in l2:
    if i not in lcomm:
      lcomm.append(i)
  else:
    luni.append(i)

for i in l2:
  if i not in l1:
    if i not in luni:
      luni.append(i)

print l1
print l2
print lcomm
print luni
