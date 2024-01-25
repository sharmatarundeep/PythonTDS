s="hi, my name is tarun. i work at arista"
print s
noe=len(s)
suni=""
for i in s:
  if i not in suni:
    suni=suni+i
print suni # hi, mynaestru.wok
max=1
charneeded=""
for i in suni:
  count=s.count(i)
  print i + " is present " + str(count) + " times"  
  temp=0
  if count > max:
    charneeded=i
    temp=count
    count=max
    max=temp
print charneeded + " is the char with maximum occurence which is " + str(max) + " times"

