# Copyright (c) 2018 Arista Networks, Inc.  All rights reserved.
# Arista Networks, Inc. Confidential and Proprietary.

#!/usr/bin/python

import pexpect,timeit,datetime as dt
import sys,time,random
switch='bn202'
#switch='sr399'
#switch='ro157.cs1'

child = pexpect.spawn("ssh admin@"+switch,timeout=100)

child.expect("#")
child.sendline("enable")
child.expect("#")
child.sendline("term len 0")
child.expect("#")
child.sendline("conf t")
child.expect("#")
child.sendline("inter po30")
child.expect("#")
for i in xrange(1,4001):
    child.sendline("shut")
    child.expect("#")
    child.sendline("no shut")
    child.expect("#")
    print i
child.sendline('exit')
child.expect("#")
child.close()
