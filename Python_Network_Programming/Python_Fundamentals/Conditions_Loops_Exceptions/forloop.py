l=["cisco", "arista","avaya","hp","juniper"]
print(l)

for a in l:
    print(a)

#using range to iterate
for a in range(len(l)):
    print(l[a])

#use enumerate func to use track index of each element
for index,element in enumerate(l):
    print(index,element)


