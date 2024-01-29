# search method is used to find pattern in entire string
mystr = "You can learn any programming language, whether its Python2, Python3, Perl, Java, javascript or PHP."
import re
a = re.search("can", mystr)
print (a.group())
a = re.search("Can", mystr, re.I) # use optional flag for considering both lower/upper case
print (a.group())

#lets practice on ARP entry
arp = "22.22.22.1   0    b4:a9:5a:ff:c8:45 VLAN#222   L"
a = re.search(r"(.+?) +(\d) +(.+?)\s{2,} (\w)*",arp)
print(a.group(1))
print(a.group(2))
print(a.group(3))
print(a.group(4))
print(a.group())
print(a.groups())

#lets practice more on ARP entry
arp = "22.22.22.1   0    b4:a9:5a:ff:c8:45 VLAN#222   L"
a = re.search(r"(.+?) +(\d) +(.+?) +(.+?) +(\w)*",arp)
print(a.groups())