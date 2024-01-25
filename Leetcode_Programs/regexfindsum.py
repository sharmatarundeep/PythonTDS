import re
s="Hello 123 and hello 321"
pat="\d+"
cpat=re.compile(pat)
l=re.findall(cpat,s)
print l
sum=0
for i in l:
  sum=sum+int(i)
print sum

