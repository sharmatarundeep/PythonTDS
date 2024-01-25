'''
var=10
def func1():
    print("inside the fucn from the module I created")
print("This will always be excuted one time when module is imported")'''

#skip the execution of some code in module while importing
var=10
def func1():
    print("inside the fucn from the module I created")
if __name__ == "__main__":
    print("This will always be excuted one time when module is imported")