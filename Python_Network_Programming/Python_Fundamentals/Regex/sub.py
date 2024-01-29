#replace a pattern occurence with something else
import re
arp = "22.22.22.1   0    b4:a9:5a:ff:c8:45 VLAN#222   L"
b = re.sub(r"\d","7", arp) # find pattern and replace with 7 in arp string
print(b)
