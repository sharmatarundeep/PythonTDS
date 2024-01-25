# Copyright (c) 2018 Arista Networks, Inc.  All rights reserved.
# Arista Networks, Inc. Confidential and Proprietary.

#!/usr/bin/python

import pexpect,timeit,datetime as dt
import sys,time,random
switch='lyv251'
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
child.sendline("ip access-list bigp24k")
child.expect("#")
for i in xrange(1,2):
  for j in xrange(1,2):
    srcip="103.1."+str(i)+"."+str(j)
    dstip="203.1."+str(i)+"."+str(j)
    child.sendline("permit ip host "+str(srcip)+" host "+str(dstip))
    child.expect("#")
child.sendline('exit')
child.expect("#")
child.close()
