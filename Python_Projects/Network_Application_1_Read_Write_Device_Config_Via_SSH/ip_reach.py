# Check the reachability of all devices , we need to make sure all the ip addresses mentioned in ip.txt file are reachable
import sys
import subprocess

#check ip reachability
def ip_reach(iplist):
    for ip in iplist:
        ip = ip.rstrip("\n")
        #print (ip) # just to check

        ping_reply = subprocess.call('ping %s -c 2' % ip, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, shell=True)

        #print (ping_reply) # just to check

        if ping_reply == 0: # 0 is for echo reply 
            print ("Device is reachable: ", ip)
        else:
            print ("Device is not reachable: ", ip)
            sys.exit()

#ip_reach(['172.30.190.25\n', '172.30.190.32\n', '172.30.190.31\n']) # just for testing