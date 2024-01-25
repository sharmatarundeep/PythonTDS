a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

#find unique between both lists and store in a new list 

#method 1 
l=a+b
s=set(l)
l=list(s)
print a
print b
print s
print l

