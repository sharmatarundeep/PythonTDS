s="hello, aditi i am tarun"
print s
s1=""
sdup=""
for i in s:
  if i not in s1:
    s1=s1+i
  else:
    if i not in sdup:
      sdup=sdup+i
      print i + " is duplicate"


    
  
