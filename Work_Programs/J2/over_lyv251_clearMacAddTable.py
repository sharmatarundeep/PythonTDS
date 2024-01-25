# Copyright (c) 2018 Arista Networks, Inc.  All rights reserved.
# Arista Networks, Inc. Confidential and Proprietary.

#!/usr/bin/python

import pexpect,timeit,datetime as dt
import sys,time,random
switch='lyv251'

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
    child.sendline("clear mac address-table dynamic")
    child.expect("#")
    #child.sendline("show mac address-table dynamic")
    #child.expect("#")
    print i
    #time.sleep(2)
    #child.sendline("show mac address-table dynamic")
    #child.expect("#")

child.sendline('exit')
child.expect("#")
child.close()
