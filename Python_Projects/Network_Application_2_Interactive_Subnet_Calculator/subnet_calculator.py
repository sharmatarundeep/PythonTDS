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

        # Task 1 : Lets find wildcard mask and no of valid hosts per subnet in the next section
        # We are going to convert subnet mask to binary.  Example 255.255.255.0 - > 11111111111111111111111100000000
        
        # Convert mast to binary string 
        mask_octets_binary = [] # we will store all the binary octets in this list

        for octets in sub_octets:
            binary_octet = bin(int(octets)).lstrip("0b") # also remove 0b from '0b11111111'
            mask_octets_binary.append(binary_octet.zfill(8)) #  To fill/padd 0's until the octet lenght becomes 8. If you convert 0 to binary it will be '0b0'. So extra 7 0's needed to be added
        
        binary_mask_value = "".join(mask_octets_binary)
        # print (mask_octets_binary) # result for 255.255.255.0 -> ['11111111', '11111111', '11111111', '00000000']
        # print (binary_mask_value) # result for 255.255.255.0 -> 11111111111111111111111100000000
        # Count host and network bits in the final binary mask
        no_zeros = binary_mask_value.count("0") # 
        no_ones = 32 - no_zeros
        # no of host = 2 raise to the power no of host bits (0's) - 2 (one for network address and one for broadcast address)
        no_host = abs(2 ** no_zeros - 2) # absolute is used to always return a positive value. This is to handle the case of /32 , no_zeros would be 0, so 2 raise to power 0 = 1 and 1 -2 = -1. 
        #print (no_zeros)
        #print (no_host)

        # Now lets find wild card mask. Formula is 255.255.255.255 minus network subnet mask 255.255.255.255 => 0.0.0.255
        wild_card_octets = []
        for octets in sub_octets:
            wild_card_octets.append(str(255 - int(octets)))
        wild_card_mask = ".".join(wild_card_octets) #
        # print (wild_card_mask)

        # Task 2 : Lets find network address and broadcast address
        # For network address make all the host bits = 0
        # For host address make all the host bits = 1

        # convert IP address provided by used to binary 
        ip_octets_binary = []
        for octets in ip_octets:
            binary_octet = bin(int(octets)).lstrip("0b")
            ip_octets_binary.append(binary_octet.zfill(8))
        # print (ip_octets_binary) # for 10.1.1.1 -> ['00001010', '00000001', '00000001', '00000001']
        ip_add_binary = "".join(ip_octets_binary)
        # print (ip_add_binary) # 00001010000000010000000100000001

        #Now to get the network address, from the ip add binary string take all until number of ones and for remaining add 0's equal to number of host bits.
        network_address = ip_add_binary[:no_ones] + "0" * no_zeros
        # print (network_address) # 00001010000000010000000100000000
        
        # now lets try to get broadcast address, from the ip add binary string take all until number of ones and for remaining add 1's equal to number of host bits.
        broadcast_address = ip_add_binary[:no_ones] + "1" * no_zeros
        #print (broadcast_address) # 00001010000000010000000111111111
        
        #now convert the network address string to ip add format. First make a list of 4 octets and then converting binary to integer
        #get 4 octets 
        network_address_octets = []
        for x in range (0,32,8):
            network_address_octets.append(network_address[x:x+8])
        # print (network_address_octets) # ['00001010', '00000001', '00000001', '00000000']
        # Now convert 4 octets into int
        network_address_int = []
        for x in network_address_octets:
            network_address_int.append(str(int(x,2))) # base 2 for integer
        # print (network_address_int) # ['10', '1', '1', '0']
        network_address_ip = ".".join(network_address_int)
        #print (network_address_ip) # 10.1.1.0

        #now convert the broadcast address string to ip add format. First make a list of 4 octets and then converting binary to integer
        #get 4 octets 
        brocast_address_octets = []
        for x in range (0,32,8):
            brocast_address_octets.append(broadcast_address[x:x+8])
        # Now convert 4 octets into int
        broadcast_address_int = []
        for x in brocast_address_octets:
            broadcast_address_int.append(str(int(x,2))) # base 2 for integer
        broadcast_address_ip = ".".join(broadcast_address_int)
        #print (broadcast_address_ip) # 10.1.1.255

        #Final print statements
        print ("\nNetwork address is : %s" % network_address_ip)
        print ("Broadcast address is : %s" % broadcast_address_ip)
        print("Number of valid hosts per subnet: %s" % no_host)
        print("Wildcard mask: %s" % wild_card_mask)
        print("Mask bits like /24 or /16 is : %s" % no_ones)
        

    except KeyboardInterrupt:
        print ("\nProgram aborted by the user..Exiting..\n")
        sys.exit()


subnet_calc() # just for testing
