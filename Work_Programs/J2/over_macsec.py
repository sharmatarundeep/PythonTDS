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
#for i in xrange(1,100000000000):
while True:
    child.sendline("int eth 6/2/1-7/47/1")
    child.expect("#")
    child.sendline("mac security profile test2")
    child.expect("#")
    time.sleep(2)
    child.sendline("no mac security profile test2")
    child.expect("#")
    child.sendline("int eth 8/2/1-9/47/1")
    child.expect("#")
    child.sendline("mac security profile test2")
    child.expect("#")
    time.sleep(2)
    child.sendline("no mac security profile test2")
    child.expect("#")

child.sendline('exit')
child.expect("#")
child.close()
