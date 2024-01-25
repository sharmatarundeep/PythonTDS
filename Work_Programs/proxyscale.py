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

for i in xrange(25,49):
  child.sendline("inter eth 8/" + str(i))
  child.expect("#")
  child.sendline("sw")
  child.expect("#")
  child.sendline("sw ac vlan  "+str(i+496))
  child.expect("#")

child.sendline('exit')
child.expect("#")
child.close()
