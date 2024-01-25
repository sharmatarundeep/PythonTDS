# Basic defination 
def sum(a,b): #define the working of a function, this func needs 2 parameters
  s=a+b
  return s # return a value
print sum(1,2) # calling a function 

#default value, if user doesnot pass parameter use default
def sum1(a=0,b=0):
  s1=a+b
  return s1
print sum1(1)

#arbitrary argument , if you are not sure about num of arguments
def sum2(*a):
  print a  
  s2=0
  for i in a:
    s2=s2+i
  return s2
print sum2(1,2,3)
