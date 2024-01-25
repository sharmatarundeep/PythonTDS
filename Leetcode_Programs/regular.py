import re
s="my name is tarun, my phone number is 6504506154 and house number is 418"
print s

#search a pattern and return true or false
pat="\d+"
cpat=re.compile(pat)
if re.search(cpat,s):
  print "string has integers"

#find values and return values
pat="\d+"
cpat=re.compile(pat)
l=re.findall(cpat,s)
print l#['6504506154', '418']

#replace matched pattern by something one time
pat="\d+"
cpat=re.compile(pat)
s1=re.sub(cpat,"6504500335",s,1)#search cpat and replace the first occurence by 6504500335
print s1#my name is tarun, my phone number is 6504500335 and house number is 418

#replace all matched by something
pat="\d+"
cpat=re.compile(pat)
s2=re.sub(cpat,"NONE",s)#search cpat and replace the first occurence by 6504500335
print s2
