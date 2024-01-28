#remove the duplicates
s="helllo my name is tarun and i work at arista"
suni=""

for i in s:
  if i not in suni:
    suni=suni+i

print(s)
print(suni)

# count the occurence of each character in string
for i in suni:
  count=0
  print(i + " is present " + str(s.count(i)) + " times")
