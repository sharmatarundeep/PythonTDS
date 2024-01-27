a = 10
print(id(a))
print(id(10))
# will be same as they both point to same memory location

b = a
print(id(b))
# will be same as ID of a as they both point to 10's memory location

b = 20
print(id(b))
# now different as b now point to 20 not 10

x = 10
y = 20
z = 10
print(id(x),id(y),id(z))
