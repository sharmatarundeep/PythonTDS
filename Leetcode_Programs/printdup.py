def printdup(s):
  suni=""
  for i in s:
    if i not in suni:
      suni=suni+i
  print suni
  for i in suni:
    if s.count(i)>1:
      print i + " is present more than once" 
s="hello my name is tarun"
print s
printdup(s)  
