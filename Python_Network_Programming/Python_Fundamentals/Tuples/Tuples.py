tup1 = (1,2,3,4)
print(type(tup1))
print(tup1[-1])

# error as its immutable
# tup1[1]=10
print(tup1)

#tuple assignment
(a,b,c) = (10,20,30)
print(a,b,c)

#both tuple should have same # of elements
#(a,b,c) = (10,20,30,40) => error

t1=(a,b,c,1,2,[10,20])
print(t1)
del t1 # to delete a tuple all together
# error print(t1) # error not defined