class person:
  def __init__(self,name,age):
    self.name=name
    self.age=age
  def printall(self):
    print self.name
    print self.age
p1= person("Tarun", 30)
#p1.printall()

class student(person):
  pass
s1=student("John", 22)
#s1.printall()

class employee(person):
  def __init__(self,name,age,empid):
    person.__init__(self,name,age)
    self.empid=empid
  def printall1(self):
    print self.name
    print self.age
    print self.empid
e1=employee("tarun",31,10001)
e1.printall()# this will only print name and age
print e1.empid # this will print empid
e1.printall1()

