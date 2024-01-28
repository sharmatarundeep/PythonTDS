# count the occurence of each element in the string
s="hi, my name is tarun. i work at arista"
print(s)
noe=len(s)
suni=""
for i in range(0,noe):
  count=1
  # To not count same character again we created a new string and will keep adding unique characters there
  if s[i] not in suni:
    suni=suni+s[i]
    for j in range(i+1,noe):
      if s[i]==s[j]:
        count=count+1
    print(s[i] +" is present " + str(count) + " times")
