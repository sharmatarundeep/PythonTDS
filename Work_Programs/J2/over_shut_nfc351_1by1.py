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
while True:
    i = random.randint(1,37)
    j = random.randint(1,37)
    print i
    child.sendline("inter eth 5/" + str(i) + "/1,6/" + str(j) + "/1")
    child.expect("#")
    child.sendline("shut")
    child.expect("#")
    time.sleep(1)
    child.sendline("no shut")
    child.expect("#")
    time.sleep(2)

child.sendline('exit')
child.expect("#")
child.close()
