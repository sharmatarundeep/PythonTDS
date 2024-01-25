# Copyright (c) 2018 Arista Networks, Inc.  All rights reserved.
# Arista Networks, Inc. Confidential and Proprietary.

#!/usr/bin/python

import pexpect,timeit,datetime as dt
import sys,time,random
switch='nfc351'

child = pexpect.spawn("ssh admin@"+switch,timeout=120)

child.expect(">")
child.sendline("enable")
child.expect("#")
child.sendline("term len 0")
child.expect("#")
child.sendline("conf t")
child.expect("#")
'''
for i in xrange(1,49):
    child.sendline("vrf definition vrf" + str(i))
    child.expect("#")
    child.sendline("ip routing vrf vrf" + str(i))
    child.expect("#")

for i in xrange(1,49):
    child.sendline("inter eth 8/" + str(i) + "/1,9/"+ str(i+1) + "/1")
    child.expect("#")
    child.sendline("vrf forwarding vrf" + str(i))
    child.expect("#")

for i in xrange(1,49):
    child.sendline("inter eth 8/" + str(i) + "/1")
    child.expect("#")
    child.sendline("ip address 8." + str(i) +  ".1.1/24")
    child.expect("#")
    child.sendline("inter eth 9/" + str(i) + "/1")
    child.expect("#")
    child.sendline("ip address 9." + str(i) +  ".1.1/24")
    child.expect("#")
'''
for i in xrange(1,49):
   child.sendline("ip route vrf vrf"+str(i)+ " 9.48.1.2/32 9." + str(i+1) +  ".1.2")
   child.sendline("ip route vrf vrf"+str(i)+ " 8.1.1.2/32 8." + str(i) +  ".1.2")
'''
for i in xrange(1,49):
   child.sendline("arp vrf vrf"+str(i)+ " 9." + str(i+1) +  ".1.2 7483.ef02.0d2e arpa")
   child.sendline("arp vrf vrf"+str(i)+ " 8." + str(i) +  ".1.2 7483.ef02.0d2e arpa")
'''
child.sendline('exit')
child.expect("#")
child.close()
