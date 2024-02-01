# decorator is a function that takes another func as parameter and extend functions functionality without modifying it

def my_decorator (target_func):
    def func_wrapper():
        return "python is such a " + target_func() + " language"
    return func_wrapper

@my_decorator
def target_func():
    return "cool"

a = target_func()
print (a)