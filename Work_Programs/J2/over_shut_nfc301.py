# Copyright (c) 2018 Arista Networks, Inc.  All rights reserved.
# Arista Networks, Inc. Confidential and Proprietary.

#!/usr/bin/python

import pexpect,timeit,datetime as dt
import sys,time,random
switch='nfc301'

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
    r = random.randint(1,49)
    print r
    child.sendline("inter eth 3/" + str(r) + "/1 , 4/"+ str(r) + "/1")
    child.expect("#")
    child.sendline("shut")
    child.expect("#")
    time.sleep(1)
    child.sendline("no shut")
    child.expect("#")
    time.sleep(2)
    child.sendline("no sw")
    child.expect("#")
    time.sleep(1)
    child.sendline("sw")
    child.expect("#")
    time.sleep(2)

child.sendline('exit')
child.expect("#")
child.close()
