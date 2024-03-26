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
# ? - pattern can occur zero or one time 
batRegex = re.compile(r'Bat(wo)?man') # this will match Batman or Batwoman - wo can occur zero or one time
mo = batRegex.search("The adventures of Batman")
print(mo.group()) # Batman
mo = batRegex.search("The adventures of Batwoman")
print(mo.group()) # Batwoman
mo = batRegex.search("The adventures of Batwowowoman") # error or no match case
print (mo) # None
# print(mo.group()) - error as wo can be just one or zero times

# * - pattern can occur zero or more times
batRegex = re.compile(r'Bat(wo)*man') # this will match Batman or Batwoman - wo can occur zero or one time
mo = batRegex.search("The adventures of Batman")
print(mo.group()) # Batman
mo = batRegex.search("The adventures of Batwoman")
print(mo.group()) # Batwoman
mo = batRegex.search("The adventures of Batwowowoman")
print(mo.group()) # Batwowowoman

# + - pattern can occur one or more times
batRegex = re.compile(r'Bat(wo)+man') # this will match Batman or Batwoman - wo can occur zero or one time
mo = batRegex.search("The adventures of Batman") # error case as no match
print(mo) # None
mo = batRegex.search("The adventures of Batwoman")
print(mo.group()) # Batwoman
mo = batRegex.search("The adventures of Batwowowoman")
print(mo.group()) # Batwowowoman

# Match exactly a few times like 3 times 
haRegex = re.compile(r'(ha){3}') # means match ha 3 times
mo = haRegex.search("he said hahaha")
print(mo.group()) # hahaha

# Match exactly in a range like 3 to 5 times
haRegex = re.compile(r'(ha){3,5}') # means match ha 3 times
mo = haRegex.search("he said hahaha")
print(mo.group()) # hahaha 
mo = haRegex.search("he said hahahahaha")
print(mo.group()) # hahahahaha

# {3,5} - 3 to 5 times, {,5} - 0 to 5 times, {3,} - atleast 3 times 
digitRegex = re.compile(r"(\d){3,5}")
mo = digitRegex.search("1234567890")
print(mo.group()) # 12345 - only 5 characters were matched
digitRegex = re.compile(r"(\d){3,}")
mo = digitRegex.search("1234567890")
print(mo.group()) # 1234567890 - march all 


# Section 4 
# Findall method - all matches of the pattern in a string

# Section 5 
# carrot character to search something at the start of a string 
beginRegex = re.compile(r"^Hello")
mo = beginRegex.search("Hello there")
print(mo.group())
mo = beginRegex.search("Hi Hello there")
print(mo)# None as Hello is not in the beginning 

# Dollar character to search something at the end of a string 
endRegex = re.compile(r"World!$")
mo = endRegex.search("Hello World!")
print(mo.group()) 
