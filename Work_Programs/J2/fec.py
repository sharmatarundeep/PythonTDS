# Copyright (c) 2018 Arista Networks, Inc.  All rights reserved.
# Arista Networks, Inc. Confidential and Proprietary.

#!/usr/bin/python

import pexpect,timeit,datetime as dt
import sys,time,random
switch='smm151'

child = pexpect.spawn("ssh admin@"+switch,timeout=120)

child.expect(">")
child.sendline("enable")
child.expect("#")
child.sendline("term len 0")
child.expect("#")
child.sendline("conf t")
child.expect("#")
while True:
    print "hello"
    child.sendline("inter eth 3/1-32/1")
    child.expect("#")
    child.sendline("error-correction encoding reed-solomon")
    child.expect("#")
    time.sleep(15)
    child.sendline("no error-correction encoding")
    child.expect("#")
    time.sleep(15)
    child.sendline("default error-correction encoding")
    child.expect("#")
    time.sleep(15)

child.sendline('exit')
child.expect("#")
child.close()
