# swap the integer values

a=10
b=20

print ("Before swapping " + "a is " + str(a) + " & b is " + str (b))

''' Method 1 
a,b=b,a
print ("After swapping " + "a is " + str(a) + " & b is " + str (b))'''

# Method 2
a = a+b
b = a-b
a = a-b
print ("After swapping " + "a is " + str(a) + " & b is " + str (b))


