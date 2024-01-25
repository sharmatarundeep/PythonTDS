w1=raw_input("enter word1")
w2=raw_input("enter word2")

if len(w1) != len(w2):
  print "length of 2 words are different, they cannot be anagrams"
  exit()

count=0
for i in w1:
  if i not in w2:
    print "2 words are not anagrams"
    exit()
  else:
    count = count+1
if count == len(w1):
  print " Yes, 2 words are anagrams"

