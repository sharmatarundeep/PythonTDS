w1=raw_input("enter word1")
w2=raw_input("enter word2")

if len(w1)!=len(w2):
  print "not anageram"
  exit()
count=0
for i in w1:
  if i in w2:
    w2=w2.replace(i,"")
    count=count+1
  else:
    print "not anagram"
    exit()
print w1 
print w2
if count == len(w1):
  print "yes angram"
