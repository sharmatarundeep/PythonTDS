import random
import sys

def subnet_calc():
    try: # to handle any keyboard interupt excpetion 
        print("\n")

        #Get ip address input from the user and check its valid or not
        ip_address = input("Enter an ip address: ")
        ip_octets = ip_address.split(".")
        if len(ip_octets) != 4: # first check number of octets 
            print ("Not a valid ip address, as the number of octets are not 4")
            sys.exit()
        for a in ip_octets: # Now check if each octet is between 0 and 255
            if (1 <= int(a) <= 255):
                continue
            else:
                print ("Not a valid ip address, as octets are not between 0 and 255\n")
                sys.exit()
        
        #Get subnet mask input from the user and check its valid or not
        subnet_mask = input("Enter a subnet mask: ")
        sub_octets = subnet_mask.split(".")
        masks = [255,254,252,248,240,224,192,128,0] # Valid list of subnet mask octets
        # 4 conditions for subnet mask to be valid. 
        # 1. Octets should be 4, 2. First octet 255, 3.  All octets value are present in masks list, 
        # 4. Any octet should be less than or equal to previous octet
        while True:
            if (len(sub_octets) == 4) and (int(sub_octets[0]) == 255) and (int(sub_octets[1]) in masks) and (int(sub_octets[2]) in masks) and (int(sub_octets[3]) in masks) and (int(sub_octets[0]) >= int(sub_octets[1])) and (int(sub_octets[1]) >= int(sub_octets[2])) and (int(sub_octets[2]) >= int(sub_octets[3])):
                break
            else:
                print ("Not a valid subnet mask.. Exiting..\n")
                sys.exit()
        

    except KeyboardInterrupt:
        print ("\nProgram aborted by the user..Exiting..\n")
        sys.exit()


subnet_calc() # just for testing
