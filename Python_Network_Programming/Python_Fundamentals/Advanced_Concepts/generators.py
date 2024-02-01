# Use to control behavior of a loop, you can suspend and resume the loop from the same point
def my_gen (x,y):
    for i in range(x):
        print ("I is : ", i)
        print ("Y is : ", y)
        yield i * y

my_gen_object = my_gen(10,5)
print (type(my_gen_object))

print (next(my_gen_object))
print (next(my_gen_object))
print (next(my_gen_object))
print (next(my_gen_object))
print (next(my_gen_object))
print (next(my_gen_object))
print (next(my_gen_object))
print (next(my_gen_object))
print (next(my_gen_object))
print (next(my_gen_object))
# print (next(my_gen_object)) # error sequence ended

#generator expression
gen_exp = (x for x in range(5))
print(type(gen_exp))
print(next(gen_exp))
print(next(gen_exp))
print(next(gen_exp))
print(next(gen_exp))
print(next(gen_exp))
# print(next(gen_exp)) # error sequence ended