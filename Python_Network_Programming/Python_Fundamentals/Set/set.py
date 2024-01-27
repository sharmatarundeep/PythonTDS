set1 = {1, 2, 3, 4, 5}
set2 = {2, 4, 6, 9}

print(set1)
print(set2)

set1.add(6)
print(type(set1))
print(set1)

list1=(1,2,3,10)
fs1=frozenset(list1)
print(fs1)
print(type(fs1))
#fs1.add(15) # error
print(fs1)