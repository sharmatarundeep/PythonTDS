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
for i in xrange(1,49):
#while True:
    '''r1 = random.randint(1,49)
    r2 = random.randint(1,49)
    print r1
    print r2'''
    print i
    child.sendline("no locator-led interface et 10/"+ str(i) + "/1")
    child.expect("#")
    time.sleep(1)

child.sendline('exit')
child.expect("#")
child.close()
