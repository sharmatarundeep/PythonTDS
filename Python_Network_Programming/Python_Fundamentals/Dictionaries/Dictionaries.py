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

#print key and value out using items function 
for k,v in dict1.items():
    print(k,v)
#or print like a tuple
for i in dict1.items():
    print(i)  

my_dict = {1: "Cisco", 2: "HP", 3: "Juniper", 4: "Arista", 5: "Avaya"}
l=my_dict.values() # form a list of dictionary values
print(l)

# Get method - Take 2 arguments Key and Default, return value corresponding to the key, if key is not there then return default specified
my_dict = {1: "Cisco", 2: "HP", 3: "Juniper", 4: "Arista", 5: "Avaya"}
print (my_dict.get(3, 0)) # If key 3 doesn't exist then return default 0

# setdefault method - set a new key and value if key doesn't exist already, if key exist do nothings
my_dict = {1: "Cisco", 2: "HP", 3: "Juniper", 4: "Arista", 5: "Avaya"}
my_dict.setdefault(6, "Nokia") # this will check if key 6 exist or not, if not then add it to dictionary. Will not do anything if key exist
print(my_dict)
