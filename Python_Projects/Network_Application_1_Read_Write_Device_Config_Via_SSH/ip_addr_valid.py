# Check if the IP address specified are valid or not
import sys

# checking octets for each IP address in the list
def ip_addr_valid(iplist):
    for ip in iplist:
        ip.rstrip("\n") # remove next line from each ip in the for loop
        octet_list = ip.split(".")

        # Check if total octets are 4 and each octet is between 0 and 255
        if (len(octet_list) == 4 and (1 <= int(octet_list[0]) <=255) and (0 <= int(octet_list[1]) <= 255) and (0 <= int(octet_list[2]) <= 255) and (0 <= int(octet_list[3]) <= 255)):
            print(" Valid IP address", ip)
            continue
        else:
            print(" Invalid IP address detected", ip)
            sys.exit()

#ip_addr_valid(['172.30.190.25\n', '172.30.190.32\n', '172.30.190.31\n']) # just for testing
#ip_addr_valid(['172.190.25\n', '172.30.190.32\n', '172.30.190.31\n']) # just for testing