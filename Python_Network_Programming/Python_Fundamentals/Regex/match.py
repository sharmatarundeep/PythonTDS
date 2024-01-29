# Match method is used to find pattern in beginning of a string
mystr = "You can learn any programming language, whether its Python2, Python3, Perl, Java, javascript or PHP."
import re
a = re.match("You", mystr) # match will just match the beginning of string
print (a) # return a match object

a = re.match("abc", mystr)
print (a) # None will be printed or returned as pattern was not matched

a = re.match("can", mystr)
print (a) # None will be printed or returned as pattern was not matched. Match will just match beginning of the string

a = re.match("You", mystr)
print (a) # return a match object

a = re.match("You", mystr)
print (a.group()) # return the matched substring in the string