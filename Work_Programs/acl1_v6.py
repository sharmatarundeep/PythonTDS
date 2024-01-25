# Copyright (c) 2018 Arista Networks, Inc.  All rights reserved.
# Arista Networks, Inc. Confidential and Proprietary.

#!/usr/bin/python

import pexpect,timeit,datetime as dt
import sys,time,random
switch='ph104'
#switch='sr399'
#switch='ro157.cs1'

child = pexpect.spawn("ssh admin@"+switch,timeout=120)

#child.expect(">")
#child.sendline("enable")
child.expect("#")
child.sendline("term len 0")
child.expect("#")
child.sendline("conf t")
child.expect("#")
child.sendline("ipv6 access-list bigp12k")
child.expect("#")
for i in xrange(1,94):
  for j in xrange(1,136):
    print j
    srcip="100:1:"+str(i)+":"+str(j)+"::1/64"
    dstip="200:1:"+str(i)+":"+str(j)+"::1/64"
    child.sendline("permit ipv6  "+str(srcip)+"  "+str(dstip))
    child.expect("#")
child.sendline('exit')
child.expect("#")
child.close()
