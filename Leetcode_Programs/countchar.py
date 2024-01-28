s="hi, my name is tarun. I work at Arista"
print(s)
s1=s.upper()#HI, MY NAME IS TARUN. I WORK AT ARISTA
s2=s.lower()#hi, my name is tarun. i work at arista
print(s1)
print(s2)
c=input("Enter the character you want to count\n")
count=0
for i in s2:
  if i==c:
   count =count+1
print(c + " is present " + str(count) + " times")

