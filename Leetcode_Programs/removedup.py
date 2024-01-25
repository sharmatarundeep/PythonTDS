s="hello my name is tarun"

s1=set(s)
s1="".join(s1)

s2=""
for i in s:
  if i not in s2:
    s2=s2+i

print s
print s1
print s2
