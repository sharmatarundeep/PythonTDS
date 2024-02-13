# Case 2 - Running a local python script via a remote server. Example run a script present on your laptop via remote server st101.
# This is just a sample script which we will run via remote server

import subprocess
import sys

ip = "172.30.190.31" # smm353's IP address 

# Just ping the IP listed above
ping_reply = subprocess.call('ping %s -c 2' % ip, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, shell=True)

if ping_reply == 0: # 0 is for echo reply 
    print ("Device is reachable: ", ip)
else:
    print ("Device is not reachable: ", ip)
    sys.exit()


# Now from you MacOS terminal do the following. This is to run this local script from remote server
# more Case2_remote_ping_script.py | ssh tarundeep@st101 python3 # Total 2 commands here -  Run this script from st101 server in python3
# OR
# cat Case2_remote_ping_script.py | ssh tarundeep@st101 python3
# Example below
'''tarundeep@Tarundeeps-MacBook-Pro-2 Running_Python_Code_Remotely % more Case2_remote_ping_script.py | ssh tarundeep@st101 python3
tarundeep@st101's password:
Device is reachable:  172.30.190.31
tarundeep@Tarundeeps-MacBook-Pro-2 Running_Python_Code_Remotely %'''
