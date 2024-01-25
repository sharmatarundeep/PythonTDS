s="hi, my name is tarun i work at arista"
print s
l=s.split()
print l # ['hi,', 'my', 'name', 'is', 'tarun', 'i', 'work', 'at', 'arista']
l1=[]
count=0
noe=len(l)
longestword=l[0]
for i in range(1,noe):
  if len(l[i]) > len(longestword):
    longestword=l[i]
print longestword + " is the longest word with length " + str(len(longestword))
