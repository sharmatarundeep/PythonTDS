l=[1,1]
t = 15 # total elements we want to find in Fibonacci series
count=2
for i in range (0,t+1):
  l.append(l[i]+l[i+1])
  count = count + 1
  if count ==15:
    break
print l
print len(l) 
