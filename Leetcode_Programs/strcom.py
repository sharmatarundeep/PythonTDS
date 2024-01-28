s1= "hello"
s2="hi"

for i in s2: 
  if i in s1:
    s1=s1.replace(i,"")

print(s1)
print(s2)
  
