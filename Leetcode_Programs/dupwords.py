s="hello, i aditi i i am tarun tarun"
print s
l=s.split()
print l# ['hello,', 'aditi', 'i', 'i', 'am', 'tarun', 'tarun']
luni=[]
ldup=[]
for i in l:
  if i in luni:
    if i not in ldup:
      ldup.append(i)
      print i + " is duplicate"
  else:
    luni.append(i)
