# Match IP address
import re
arp = "22.22.22.1   0    b4:a9:5a:ff:c8:45 VLAN#222   L"
a = re.findall(r"(\d+\.\d+\.\d+\.\d+)",arp)
print(a)

#many ways to represent a number
b = re.findall(r"(\d\d\.\d{2}\.[0-9][0-9]\.[0-9]{1,3})",arp)
print(b)

# find multiple occurences of same pattern
arp1 = "22.22.22.1   0    10.1.1.1 VLAN#222   L"
c = re.findall(r"\d+\.\d+\.\d+\.\d+", arp1)
print (c)
