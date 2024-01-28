a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
l=[]
#find common elements and make sure there are no duplicates

for i in a:
  if i in b:
    if i not in l: # or we can later convert list of common elements into set
      l.append(i)

print(a)
print(b)
print(l)


