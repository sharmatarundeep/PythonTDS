def maxcharstr(string):
  suni=""
  for i in string:
    if i not in suni:
      suni=suni+i  
  max=0
  for i in suni:
    if string.count(i)>max:
       char=i
       max= string.count(i)
  print "max occuring char is "+ char + " and it is present " + str(max) + " times"
print "enter a string"
s=raw_input()
maxcharstr(s)

