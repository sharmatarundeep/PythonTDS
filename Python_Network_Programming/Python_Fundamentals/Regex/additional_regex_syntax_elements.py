a = "I love Python 3"
import re

# match start of a string using ^ caret symbol
b = re.search(r"^[A-Z]\s\w{4}",a)
print (b.group())

# match end of a string using $ dollar symbol
c = re.search(r"\w{6}\s\d*",a)
print (c.group())

my_regex_str = '200.10.2.0 255.255.255.0 200.20.5.2 1 205 T#1 S IB 5'
a = re.search(r"(.+?) +\d\d(\d)\.([0-9]{2,})\.([0-9]{1,3})\.(\d) +(.+)1 +(\d{3}) +(\w{1})#.+S(\s+)(\w)\w +(.*)", my_regex_str)
print (a.group(0))