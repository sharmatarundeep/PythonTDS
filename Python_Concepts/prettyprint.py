# For better print results we can always use pprint module (pretty print :))

import pprint

message = "It was a bright cold day in April, and the clocks were striking thirteen."
count = {} # empty dictionary

for char in message:
    count.setdefault(char, 0) # initially for a character create a key,value pair in dict, with value as 0. If the key exist then do nothing
    count[char] = count[char] + 1 # later increment count value by 1 

print(count)
print("##############")
print("##############")
pprint.pprint(count)

# You can also store what pprint return into another variable using pformat function and use it later as needed
print("##############")
print("##############")
txt1 = pprint.pformat(count)
print (txt1)