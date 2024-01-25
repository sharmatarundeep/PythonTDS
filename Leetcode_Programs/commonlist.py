a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

l=[]
#find common and no duplicates

for i in a:
  if i in b:
    l.append(i)

l1=set(l) # to remove duplicate we can use set
l2=list(l1) # convert back to list
print a
print b
print l
print l1
print l2


