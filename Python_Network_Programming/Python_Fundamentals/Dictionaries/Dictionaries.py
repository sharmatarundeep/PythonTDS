dict1={"a":10,"b":20,"c":30}
print(dict1)
print(type(dict1))

print(dict1['a']) # 10
dict1['d']=40 #add a new member
print(dict1)
print(len(dict1)) # 4

dict1['d']=50 # modify a value
print(dict1)

del dict1['d'] # delete an element using key
print(dict1)
print(dict1.keys())
print(dict1.values())
print(dict1.items())

my_dict = {1: "Cisco", 2: "HP", 3: "Juniper", 4: "Arista", 5: "Avaya"}
l=my_dict.values()
print(l)