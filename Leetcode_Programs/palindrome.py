s=raw_input("Please enter a string")
rev=""
noe=len(s)
for i in s:
  rev = i  + rev
print s
print rev
if rev==s:
  print "The string entered is palindrome"
else:
  print "The string entered is not palindrome"
