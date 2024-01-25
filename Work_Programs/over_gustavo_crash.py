# Copyright (c) 2018 Arista Networks, Inc.  All rights reserved.
# Arista Networks, Inc. Confidential and Proprietary.

#!/usr/bin/python

import pexpect,timeit,datetime as dt
import sys,time,random
switch='yo657'
#switch='sr399'
#switch='ro157.cs1'

child = pexpect.spawn("ssh admin@"+switch,timeout=120)

child.expect(">")
child.sendline("enable")
child.expect("#")
child.sendline("term len 0")
child.expect("#")
child.sendline("conf t")
child.expect("#")
child.sendline("mac sec")
child.expect("#")
child.sendline("profile test2")
child.expect("#")
#for i in xrange(1,100000000000):
while True:
    child.sendline("sci")
    child.expect("#")
    child.sendline("no sci")
    child.expect("#")
    time.sleep(1)
    child.sendline("sci")
    child.expect("#")
    child.sendline("no sci")
    child.expect("#")
    time.sleep(1)
    child.sendline("sci")
    child.expect("#")
    child.sendline("no sci")
    child.expect("#")
    a = random.randint(5,7)
    print a
    time.sleep(a)
    child.sendline("sci")
    child.expect("#")
    child.sendline("no sci")
    child.expect("#")
    time.sleep(1)
    child.sendline("sci")
    child.expect("#")
    child.sendline("no sci")
    child.expect("#")
    time.sleep(1)
    child.sendline("sci")
    child.expect("#")
    child.sendline("no sci")
    child.expect("#")
    b = random.randint(36,40)
    print b
    time.sleep(b)

child.sendline('exit')
child.expect("#")
child.close()
