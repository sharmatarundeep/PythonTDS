s= "hi there my name is tarun"
s1= set(s) #now we need to find unique elements in string
l=list(s1) #output is ['a', ' ', 'e', 'i', 'h', 'm', 'n', 's', 'r', 'u', 't', 'y']
print s
print l

'''
noe=len(s)
for i in l: # now iterate list l one by one
  count=0
  for j in s: # compare element  in l with string s
    if i==j:
      count = count +1
  print i + " is present " +  str(count) + " times"
'''

for i in l: # now iterate list l one by one
  count=s.count(i)
  print i + " is present " +  str(count) + " times"
