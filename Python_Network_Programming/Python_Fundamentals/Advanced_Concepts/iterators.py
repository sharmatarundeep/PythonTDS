# use to iterate a sequence 
my_list = [1,2,3,4,5,6,7]
print(my_list)

#old way to iterate 
for x in my_list:
    print(x)

#new way - iterators
my_iter= iter(my_list)
print(type(my_iter))
print (next(my_iter)) # use next func to iterate now ==> 1
print (next(my_iter)) # 2
print (next(my_iter)) # 3
print (next(my_iter)) # 4
print (next(my_iter)) # 5
print (next(my_iter)) # 6
print (next(my_iter)) # 7
#print (next(my_iter)) # Error that iteration of sequence ended