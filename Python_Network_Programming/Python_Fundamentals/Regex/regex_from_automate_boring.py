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


# Section 2
# Parenthesis can be used to separate groups - suppose you want to separate area code and phone number
message = "Call me 415-555-1011 tomorrow, or at 415-555-1111 any time later"
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)') # Use parenthesis to separate groups
mo = phoneNumRegex.search(message)# find the matching object (mo) in the message string using regex object phoneNumRegex
print (mo.group()) # Return all groups - 415-555-1011
print (mo.group(1)) # Return first group - 415
print (mo.group(2)) # Return second group - 555-1011

# The pipe | usage - Used like a or in regex
batRegex = re.compile(r'Bat(man|mobile|copter|bat)') # this will match Batman or Batmobile or Batcopter or Batbat
mo = batRegex.search("Batmobile lost a wheel")
print(mo.group())


# Section 3 