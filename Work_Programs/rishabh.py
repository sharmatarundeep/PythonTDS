# Copyright (c) 2018 Arista Networks, Inc.  All rights reserved.
# Arista Networks, Inc. Confidential and Proprietary.

#!/usr/bin/python

import pexpect,timeit,datetime as dt
import sys,time,random
switch='bn202'
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
while True:
    child.sendline("hardware counter feature subinterface out layer2")
    child.expect("#")
    child.sendline("hardware counter feature subinterface in layer2")
    child.expect("#")
    #time.sleep(1)
    child.sendline("no hardware counter feature subinterface out layer2")
    child.expect("#")
    child.sendline("no hardware counter feature subinterface in layer2")
    child.expect("#")

child.sendline('exit')
child.expect("#")
child.close()
