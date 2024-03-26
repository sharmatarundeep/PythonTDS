#! python3 
# In Python, a shebang is the first line of a script, which specifies the interpreter that should be used to run the script.
import re 
import pyperclip # Use pip3 install pyperclip to install. Its a Python module for copy and paste clipboard functions

# Create a regex for phone number
# Phone number examples 
# 413-555-0000, 555-0000, (415) 555-0000, 555-0000 ext 12345, ext. 12345
phoneRegex = re.compile(r'''
(
((\d\d\d)|(\(\d\d\d\)))? #area code (optional) can be 3 digits or 3 digits in parenthesis
(-|\s)? #first separator which can be a space or a - (optional)
\d\d\d #3 digits
- # - separator
\d\d\d\d #last 4 digits
(\s?ext(\.)?\s\d{2,5})? #(optional) extension which can be ext or ext. (. is optional) followed by 2 to 5 digits
)''', re.VERBOSE)

#Testing the phone regex regex
#mo = phoneRegex.search("My phone is 613-207-1234 ext 12345") 
#print(mo.group()) 

# Create a regex for email address
emailRegex = re.compile(r'[a-zA-Z0-9_.+]+\@[a-zA-Z0-9_.+]+') # [a-zA-Z0-9_.+] will cover most of the scenarios used like ., + , _

#Testing the email regex regex
#mo = emailRegex.search("My phone is sha.tar@gmail.com") 
#print(mo.group()) 

# Get the text (data) from the file or the clipboard 
text = pyperclip.paste() # copy something from any file and code will paste it and store it in text 

# Extract the email and phone number 
extractPhone = phoneRegex.findall(text)
extractEmail = emailRegex.findall(text)

#extractPhone will be something like [('479-205-4874', '479', '479', '', '-', '', ''), ('678-560-3485', '678', '678', '', '-', '', '')]
#print(extractPhone) # [('479-205-4874', '479', '479', '', '-', '', ''), ('678-560-3485', '678', '678', '', '-', '', '')]
#print(extractEmail) # ['jmckay67@aol.com', 'tjordan@msn.com']

# To get just the phone numbers we will traverse the list and take out first element from each tuple
allPhoneNumbers = [] # empty list to store all phone numbers
for phoneNumber in extractPhone:
    allPhoneNumbers.append(phoneNumber[0])
# print (allPhoneNumbers) # ['479-205-4874', '678-560-3485']

# Copy the extracted data to the clip board
results = '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(extractEmail)
print (results)
pyperclip.copy(results) # After running the program, paste the output to results.txt file

