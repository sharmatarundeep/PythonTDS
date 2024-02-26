#Count number of occurrences of a letter in a string. 
#We will create a dictionary, then keep adding key/value pairs in the dictionary for each unique character.
#If we see same character again we will increment the count by 1.

message = "It was a bright cold day in April, and the clocks were striking thirteen."
count = {} # empty dictionary

for char in message:
    count.setdefault(char, 0) # initially for a character create a key,value pair in dict, with value as 0. If the key exist then do nothing
    count[char] = count[char] + 1 # later increment count value by 1 

print(count)

# if you want to ignore capital or small letter and treat them same.. convert string to al upper case and then count
count1 = {} # empty dictionary
for char in message.upper():
    count1.setdefault(char, 0) # initially for a character create a key,value pair in dict, with value as 0
    count1[char] = count1[char] + 1 # later increment count value by 1 

print("########################")
print(count1)
