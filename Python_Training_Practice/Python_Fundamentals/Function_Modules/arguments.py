# positional arguments
def func1(x,y,z):
    s=x+y+z
    return s
result = func1(1,2,3)
print(result)

#error
#result = func1(1,2)

#keyword arguments - passed in call
def func2(x,y,z):
    s=x+y+z
    return s
result = func2(x=1,y=2,z=3)
print(result)
result = func2(z=3,y=2,x=1) # order in which we pass the argument can change
print(result)

#mixing positon and keyword argument
def func3(x,y,z):
    s=x+y+z
    return s
result = func3(1,2,z=3)
print(result)
#error as first always write positional args then only keyword args come
#result = func2(x=1,y=2,3)

#default value of an parameter can also be passed
def func4(x,y,z=3):
    s=x+y+z
    return s
result = func4(1,2)
print(result)
result = func4(1,2,4)
print(result)

#what if you don't know how many parameters to pass
def func5(x,*args):
    print(x)
    print(args)
func5("hello")
func5("hello",100,200)

#if you want to get rid of tuple while printing, iterate over the tuple
def func6(x,*args):
    print(x)
    for a in args:
        print(a)
func6(10, 20, 30)


