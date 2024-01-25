s=raw_input("Enter a string: ")
print s
try:
  int(s)
except:
  print("Not all are integers")
else:
  print("all are integers")

