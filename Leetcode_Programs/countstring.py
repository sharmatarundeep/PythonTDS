# count occurence of each character in a string
s= "hi there my name is tarun"
s1= set(s) #now we need to find unique elements in string and get a set
print(s)

'''
noe=len(s)
for i in s1: # now iterate set s1 one by one
  count=0
  for j in s: # compare element  in set with string s
    if i==j:
      count = count +1
  print i + " is present " +  str(count) + " times"
'''
#for each element in set , we will count the occourence in string
for i in s1: # now iterate list l one by one
  count=s.count(i)
  print(i + " is present " +  str(count) + " times")
