# Section 1 
import re 
message = "Call me 415-555-1011 tomorrow, or at 415-555-1111 any time later"
# Extract all the phone numbers using regex
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') # compile a regex object to be used later to extract 
# Search will find the first occurrence only 
mo = phoneNumRegex.search(message)# find the matching object (mo) in the message string using regex object phoneNumRegex
print (mo.group()) # 415-555-1011 - only the first occurrence
#use findall for all occurrences 
mo = phoneNumRegex.findall(message)# find the matching object (mo) in the message string using regex object phoneNumRegex
print (mo)# findall return a list of all matching results
# you can also use regex without compiling
mo = re.findall(r'\d\d\d-\d\d\d-\d\d\d\d',message)# find the matching object (mo) in the message string using regex object phoneNumRegex
print (mo)


