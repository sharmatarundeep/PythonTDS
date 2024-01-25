from itertools import permutations
s="abc"
stringList = permutations('abc')
for i in stringList:
  print i
  print "".join(i)

