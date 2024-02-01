# suppose you have many functions in the prog, now you want to find how much time each program takes to execute
# you can add this functionality to every program , this is not scalable and right approach
# you can use decorators to add/ extend the functionality to all the functions in one go 

import time

def tictoc(func):
    def wrapper():
        t1 = time.time()
        func()
        t2 = time.time() - t1
        print(f"Took {t2} seconds")
    return wrapper

@tictoc # now when you call func1, it will run the extend functionalty also which is mentioned in tictoc decorator
def func1():
    print("this is func1")
    time.sleep(1.4)

@tictoc
def func2():
    print("this is func2")
    time.sleep(0.4) 

func1()
func2()
print("Done")