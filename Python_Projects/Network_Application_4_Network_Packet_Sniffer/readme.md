* Python Network Application # 4 - Basic Network Packet Sniffer
* Overview - Capture and decode packets using Scapy module. 
* About scapy - Scapy is a powerful interactive packet manipulation library written in Python. Scapy is able to forge or decode packets of a wide number of protocols, send them on the wire, capture them, match requests and replies etc.
* In my case I will use st101 server for this exercise and to run scapy as I am not able to run scapy on DUTs or my Macos because of permissions. Check ifconfig on st101, find loopback interface, from one terminal ping loopback's ip address, from another terminal run "sudo scapy" to use scapy.
* A few Scapy basics
    - lsc() - To find list of all the functions available in scapy
    - ls() - List of all protocols that scapy support
    - ls(ICMP) - ls with a protocol name as argument will provide structure of ICMP packet, its parameters and default metrics
    - print(sniff.__doc__) - to check all the parameters sniff func can take like count, iface, filter etc
    - pkt = sniff (iface = "lo", count =5, filter = "icmp") - sniff 5 packet on lo interface of icmp protocol
    - pkt - <Sniffed: TCP:0 UDP:0 ICMP:5 Other:0>
    - pkt.show() - will show 5 captured packets
    - pkt is a list so pkt[0] - will show details of first packet
    - pkt[0].show() - will show details of first packet but in a very clean / readable / organized way
    - pkt[0][2] - Each packet has nested list of different header layers - [2] will show just the ICMP part of packet 
    - pkt[0][ICMP] - Another way to see ICMP layer in the first packet
    - pkt[0][ICMP].show() - Better readable output of ICMP layer in first packet
    - pkt[0][ICMP].summary() - Just the summary of ICMP layer in first packet
    - pkt[0][1].src - Find source IP from IP layer of first packet


Modules used 
* os.path (for check if file exist or not)
* sys (for exiting the program in case of error sys dot exit())
* scapy (for capturing and decoding packets on the network)
* logging (to ignore some logs / warnings thrown by scapy)

<br>
Author - Tarundeep Sharma
