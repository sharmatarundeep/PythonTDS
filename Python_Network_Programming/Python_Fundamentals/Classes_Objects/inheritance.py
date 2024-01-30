from Classes_objects import MyRouter
class MyNewRouter(MyRouter):
    def __init__(self, routername, model, sno, ios, portsno):
        MyRouter.__init__(self,routername, model, sno, ios )
        self.portsno = portsno
    def print_new_router(self, string):
        print(string+self.model)

#creating objects from the inherited child class
router4 = MyNewRouter("R1", "2600", "123456","12.4", "10")
print(router4)
print(router4.model) # attribute from parent class
print(router4.portsno) # attribute from child class

#calling func from child class
router4.print_new_router("abc")

#calling func from child class
router4.print_router("Jan01,2024")