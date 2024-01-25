s=raw_input("enter a string: ")
count=0
print s
for i in s:
  if s.count(i)==1:
    print i + " is the first unique char in the string"
    exit()
  else:
    count=count+1

if count ==len(s):
   print "there is no unique char in the string"


