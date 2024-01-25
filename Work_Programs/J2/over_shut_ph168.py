# Copyright (c) 2018 Arista Networks, Inc.  All rights reserved.
# Arista Networks, Inc. Confidential and Proprietary.

#!/usr/bin/python

import pexpect,timeit,datetime as dt
import sys,time,random
switch='ph168'

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
    #r = random.randint(0,24)
    print i
    child.sendline("inter eth  3/5/1,3/6/1,3/35/1,3/36/1")
    child.expect("#")
    child.sendline("shut")
    child.expect("#")
    time.sleep(1)
    child.sendline("no shut")
    child.expect("#")
    time.sleep(15)

child.sendline('exit')
child.expect("#")
child.close()
