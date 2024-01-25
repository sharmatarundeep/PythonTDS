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
child.sendline("inter eth 9/2/1-9/35/1")
child.expect("#")
while True:
    child.sendline("mac sec profile test2")
    child.expect("#")
    time.sleep(1)
    child.sendline("no mac sec profile")
    child.expect("#")
    time.sleep(1)

child.sendline('exit')
child.expect("#")
child.close()
