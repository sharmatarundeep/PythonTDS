# Copyright (c) 2018 Arista Networks, Inc.  All rights reserved.
# Arista Networks, Inc. Confidential and Proprietary.

#!/usr/bin/python

import pexpect,timeit,datetime as dt
import sys,time,random
switch='yo657'

child = pexpect.spawn("ssh admin@"+switch,timeout=120)

child.expect(">")
child.sendline("enable")
child.expect("#")
child.sendline("term len 0")
child.expect("#")
child.sendline("conf t")
child.expect("#")
for i in xrange(1,37,2):
    child.sendline("inter eth 9/" + str(i) + "/1 , 9/"+ str(i+1) + "/1")
    child.expect("#")
    child.sendline("sw")
    child.expect("#")
    child.sendline("sw mode acc")
    child.expect("#")
    child.sendline("sw acc vlan " + str(4000+i))
    child.expect("#")

child.sendline('exit')
child.expect("#")
child.close()
