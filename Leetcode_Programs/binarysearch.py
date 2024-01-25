l=[1,3,2,4,6,5,8,10,99,15,5,2,4,23,43]

l.sort()
print l # [1, 2, 2, 3, 4, 4, 5, 5, 6, 8, 10, 15, 23, 43, 99]
n=raw_input("enter the number you want to find in list:")
if int(n) in l:
  print "number present in list"
else:
  print "number not present in list"
  exit()

noe=len(l)
first=0
last=noe
mid=(first+last)/2

for i in range(first,last):
  if l[mid]==int(n):
    print n + " is present at index " + str(mid)
    exit()
  elif l[mid]>int(n):
    last = mid
    mid = (first+last)/2
  elif l[mid]<int(n):
    first = mid
    mid = (first+last)/2


