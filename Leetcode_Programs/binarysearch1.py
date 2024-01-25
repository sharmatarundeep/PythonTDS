l=[1,3,2,99,100,23,5,6,7,9,10,11,12,13]
l.sort()
print l
n=raw_input("Enter the number you want to search:")
first =0
last =len(l)
mid = (first+last)/2

if int(n) in l: # first before searching the number just make sure its present in the list or not
  print "number present in list"
else:
  print "number not present in list" # if not present just exit
  exit()

for i in range(first,last):
  if int(n)==l[mid]:
    print "Number " + n + " is present at index " + str(mid)
    exit()
  elif int(n)>l[mid]:
    first=mid
    mid = (first+last)/2
  elif int(n)<l[mid]:
    last = mid
    mid = (first+last)/2
