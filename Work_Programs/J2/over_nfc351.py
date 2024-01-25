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
for i in xrange(1,100000000000):
#while True:
    print i
    child.sendline("monitor session s1 sou et 9/2/1-9/11/1")
    child.expect("#")
    time.sleep(1)
    child.sendline("monitor session s1 sou et 9/2/1-9/11/1 rx")
    child.expect("#")
    time.sleep(1)
    child.sendline("monitor session s1 sou et 9/2/1-9/11/1 tx")
    child.expect("#")
    time.sleep(1)

child.sendline('exit')
child.expect("#")
child.close()
