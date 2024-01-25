# Copyright (c) 2018 Arista Networks, Inc.  All rights reserved.
# Arista Networks, Inc. Confidential and Proprietary.

#!/usr/bin/python

import pexpect,timeit,datetime as dt
import sys,time,random
switch='kn257'
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
child.sendline("inter eth 1-8,49/1")
child.expect("#")
while True:
    child.sendline("shut")
    child.expect("#")
    time.sleep(1)
    child.sendline("no shut")
    child.expect("#")
    time.sleep(1)

child.sendline('exit')
child.expect("#")
child.close()
