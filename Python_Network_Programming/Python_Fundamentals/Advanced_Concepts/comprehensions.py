# List , set and dictionary comprehension

# Old way to create a list from range
list1 = []
for x in range(10):
    result = x ** 2
    list1.append(result)
print (list1)

# list comprehension - 4 lines of code replaced by 1 
list2=[x**2 for x in range(10)]
print(list2)

# list comprehension - when you want if statement too
list3 = [x**2 for x in range(10) if x > 5]
print(list3)

# set comprehension 
set1 = {x**2 for x in range(10)}
print(set1)

# dict comprehension - dict is key/value pair
dict1 = {x:x**2 for x in range(10)}
print (dict1)