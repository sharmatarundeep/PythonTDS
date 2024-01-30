class MyRouter(object):
    "class that describes the characteristics of a router"
    def __init__(self, routername, model, sno, ios):
        self.routername = routername
        self.model = model
        self.sno = sno
        self.ios = ios
    def print_router(self, manu_date):
        print("Router name is : ", self.routername)
        print("Router model is : ", self.model)
        print("Router sno is : ", self.sno)
        print("Router ios is : ", self.ios)
        print("Router model & manufacturing date is : ", self.model + manu_date)

#creating objects from a class 
router1 = MyRouter("R1", "2600", "123456","12.4")
print(router1)
router2 = MyRouter("R2", "7500", "00000","10.1")
print(router2)

#accessing the attributes of an object
print(router1.routername)
print(router1.model)
print(router1.sno)
print(router1.ios)
print(router1.ios)

#call a method which is inside a class defination
router1.print_router("Jan01,2024")
router2.print_router("May01,2024")

#change values of an object attribute
router1.ios = "0.0"
print (router1.ios)
router1.print_router("Jan01,2024")

# getattr
print (getattr(router1,"ios"))

#setattr
setattr(router1, "ios", "10.10")
print (getattr(router1,"ios"))

#hasattr
print(hasattr(router1, "ios")) # True
print(hasattr(router1, "IOS")) # False

#isinstance - To check an object is an instance of a particular class
print(isinstance(router2, MyRouter))
print(isinstance(router1, MyRouter))

print ("End of parent class")
