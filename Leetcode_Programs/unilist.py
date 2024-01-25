s="helllo my name is tarun and i work at arista"
suni=""

for i in s:
  if i not in suni:
    suni=suni+i

print s
print suni

for i in suni:
  count=0
  print i + " is present " + str(s.count(i)) + " times"
