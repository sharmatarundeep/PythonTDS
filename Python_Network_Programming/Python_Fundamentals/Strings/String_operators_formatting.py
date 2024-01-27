x = "Hi"
y = " Tarun"
print(x + y)  # concatination
print(x * 3)  # repeat string
print((x + y) * 3)  # add and then multiply
print("i" in x)  # True
print("y" in x)  # False
print("y" not in x)  # True

a = "Cisco Model: 2600XM, 2 slots, IOS 12.4"
print(a)
#in above example model, slots and IOS is dynamic. Use % operation to pass values dynamically
b = 'Cisco Model: %s, %d slots, IOS %f' % ("2600XM", 2, 12.4)
print(b)

b = "Cisco Model: %s, %d slots, IOS %f" % ("3000XM", 4, 14.4)
print(b)
b = "Cisco Model: %s, %d slots, IOS %.1f" % ("3000XM", 4, 14.4)
print(b)
b = "Cisco Model: %s, %d slots, IOS %.2f" % ("3000XM", 4, 14.4)
print(b)

b = 'Cisco Model: {}, {} slots, IOS {}'.format("2600XM", 2, 12.4)
print(b)

b = 'Cisco Model: {0}, {1} slots, IOS {2}'.format("2600XM", 2, 12.4)
print(b)

b = 'Cisco Model: {2}, {0} slots, IOS {1}'.format("2600XM", 2, 12.4)
print(b)