# Map Method 1 - Define regular func and use it with map
def product10(a):
    return a*10
r1 = range(10)
print (map(product10,r1)) # map will apply func to all the elements in the sequence, this will just return a map object 
print (list(map(product10, r1))) # to get output as a list

result = map(product10,r1) # map will apply func to all the elements in the sequence, this will just return a map object 
print (result) # return map object 
print (list (result)) # return list 

# Map Method 2 - Use lambda func
result = map(lambda a: a*10, r1)
print (result) # return map object 
print (list (result)) # return list 

# Filter - Filter all elements in the sequence for which func returns true
result = filter (lambda a: a>5, r1)
print (list (result)) # [6,7,8,9]