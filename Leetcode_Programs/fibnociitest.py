l=[1,1]
t=15
for i in range(2,t):
  l.append(l[-2]+l[-1])

print l
print len(l)
