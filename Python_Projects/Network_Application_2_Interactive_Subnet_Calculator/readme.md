* Python Network Application # 2 - Command line interactive subnet calculator. 
* Using an Ip address and subnet mask given by the user will return 5 parameters
    * Network Address (make all the host bits 0 in binary)
    * Broadcast Address (make all the host bits 1 in binary)
    * Number of valid host per subnet (Formula 2 raise to power number of host bits - 2 (for network address and broadcast address))
    * Wildcard Mask (Formula 255.255.255.255 minus subnet mask)
    * Number of mask bits (like /24, /16 - number of bits masked) (No of 1's calculated in binary of subnet mask)
    * Also we will add functionalty to generate one or more random ip addresses from a given subnet (To generate random ip we will use network address and broadcat address. Now compare all the octets in network address and broadcast added, it they are same use as is, if they are not same randomize the octet and use for generating the random IP)
* Plan 
    * Import all the modules 
    * Check ip address validity
    * Check subnet mask validity
    * If valid move to next steps 
    * Convert mask to binary, count host bit in mask and count number of host / subnet
    * Obtain the wild card mask
    * Convert ip to binary, obtain network and broadcast address from binary
    * Print all results 
    * Generate random IP address in subnet 

* Example 
* User Input 
Enter an ip address: 192.168.0.2
Enter a subnet mask: 255.255.255.0
* Application output 
Network address : 192.168.0.0
Broadcast address : 192.168.0.255
Number of valid host per subnet : 254
Wildcard mask : 0.0.0.255
Mask bits : 24
Do you want to generate random ip address from this subnet : (y/n)y
Random ip address is : 192.168.0.8
Do you want to generate random ip address from this subnet : (y/n)y
Random ip address is : 192.168.0.173
Do you want to generate random ip address from this subnet : (y/n)n
Ok, bbye!!

<br>
Author - Tarundeep Sharma
