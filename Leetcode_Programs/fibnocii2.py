l=[1,1]
t = 15 # total elements we want to find in Fibonacci series
for i in range (2,t): # we already have 2 elements , so let's start the loop with 3rd element
  l.append(l[-1]+l[-2])
print l
print len(l)
