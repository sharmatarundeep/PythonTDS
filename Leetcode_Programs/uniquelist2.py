#find unique element in one list

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

#Method 1 
'''
l=[]
for i in a:
  if i not in l:
    l.append(i)
print a
print l
'''
#Method 2
s=set(a)
l=list(s)
print a
print l


