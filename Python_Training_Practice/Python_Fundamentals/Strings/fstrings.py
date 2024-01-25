#introduced in python 3.6 to use variables in strings

model="2600XM"
slot = 2
ios = 12.4

b = f'Cisco Model: {model}, {slot} slots, IOS {ios}'
print(b)

c = f'Cisco Model: {model}, {slot * 2} slots, IOS {ios}'
print(c)

d = f'Cisco Model: {model.lower()}, {slot * 2} slots, IOS {ios}'
print(d)

