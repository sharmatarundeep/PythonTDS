#find non common elements between 2 lists
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

l=[]

for i in a:
  if i not in b:
    l.append(i)
# we have to do the operation on both the list as there can be unique elements in both
for i in b:
  if i not in a:
    l.append(i)

print(a)
print(b)
print(l)


