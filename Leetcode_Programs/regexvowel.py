import re
s="helo 23 123 44 4444 678 786786"
print s
pat="\d+" #extract all numbers
cpat=re.compile(pat)
l=re.findall(cpat,s)
print l 
leven=[]
for i in l:
  if len(i)%2==0:
    leven.append(i)
print leven#['23', '44', '4444', '786786']
