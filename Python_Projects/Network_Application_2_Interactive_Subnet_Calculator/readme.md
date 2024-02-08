* Python Network Application # 2 - Command line interactive subnet calculator. 
* Using an Ip address and subnet mask given by the user will return 5 parameters
    * Network Address 
    * Broadcast Address
    * Number of valid host per subnet 
    * Wildcard Mask
    * Number of mask bits (like /24, /16 - number of bits masked)
    * Also we will add functionalty to generate one or more random ip addresses from a given subnet
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
