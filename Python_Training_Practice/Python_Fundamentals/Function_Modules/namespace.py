# built in namespace
print(list(range(10)))

# global namespace
my_var = 10
print(my_var)

# local namespace
def func1():
    var=5
    print(var)
func1()

#error - trying to use local namespace variable globally
#print(var * 10)

#same variable name in local and global space
def func1():
    var=5 # local variable
    print(var)
func1()
var=10 # global variable
print(var)

#use global variable inside local namespace
var=10
def func1():
    global var # use this statement to import global variable locally
    print(var)
func1()

# how to use return statement and use returned local variable globally
def func2():
    var=5 # local variable
    print(var)
    return var
new_global_variable=func2()
print(new_global_variable)