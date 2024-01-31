#lamda functions
#basic example
a = lambda x, y : x *  y
print (type(a)) # function 
print (a(2,10)) # 20

# old way of creating a new list using 2 for loops and concatinating this list to another list
def myfunc(mylist):
    list_xy=[]
    for x in range(10):
        for y in range(5):
            result = x * y
            list_xy.append(result)
    return list_xy + mylist
print (myfunc([100,101,102]))

#now lets do the same with lambda func and list comprehension - in just one line
b = lambda mylist : [x * y for x in range(10) for y in range (5)] + mylist
print (b([100,101,102]))