# Anagram is a word that is made by rearranging another word
# So for 2 words to be anagram they have to be same length and have same characters
# Example Iceman and Cinema
w1=input("enter word1\n")
w2=input("enter word2\n")

if len(w1) != len(w2):
  print ("length of 2 words are different, they cannot be anagrams")
  exit()

count=0
for i in w1:
  if i not in w2:
    print("2 words are not anagrams")
    exit()
  else:
    count = count+1
if count == len(w1):
  print (" Yes, 2 words are anagrams")

