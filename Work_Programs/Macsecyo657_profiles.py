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

for i in xrange(1,6):
  for j in xrange(1,6):
    child.sendline("inter eth 5/" + str(i+9) +"/1."+str(j))
    child.expect("#")
    child.sendline("mac security profile t"+str(i))
    child.expect("#")

for i in xrange(15,18):
  for j in xrange(1,6):
    child.sendline("inter eth 5/" + str(i) +"/1."+str(j))
    child.expect("#")
    child.sendline("mac security profile t"+str(j+5))
    child.expect("#")


for i in xrange(19,21):
  for j in xrange(1,6):
    child.sendline("inter eth 5/" + str(i) +"/1."+str(j))
    child.expect("#")
    child.sendline("mac security profile t"+str(j+8))
    child.expect("#")

for i in xrange(21,26):
  for j in xrange(1,6):
    child.sendline("inter eth 5/" + str(i) +"/1."+str(j))
    child.expect("#")
    child.sendline("mac security profile t"+str(j+10))
    child.expect("#")


count= 1170
for i in xrange(27,31):
  for j in xrange(1,6):
    child.sendline("inter eth 5/" + str(i) +"/1."+str(j))
    child.expect("#")
    child.sendline("mac security profile t"+str(j+5))
    child.expect("#")



child.sendline('exit')
child.expect("#")
child.close()
