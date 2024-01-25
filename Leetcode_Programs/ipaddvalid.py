ip=raw_input("enter an ip add")

l=ip.split(".")

print l
count=0

noe = len(l)

if noe != 4:
  print "invalid ip"
  exit()

for i in l:
   if int(i)<0 or int(i)>255:
     print "invalid ip"
     exit()
   else:
     count = count +1
if count == noe:
  print "valid ip"
