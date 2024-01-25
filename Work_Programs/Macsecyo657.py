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
'''
count= 1110
for i in xrange(1,6):
  child.sendline("inter eth 5/" + str(i+10) +"/1")
  child.sendline("no sw")
  child.sendline("no shut")
  count = count+10
  for j in xrange(1,11):
    child.sendline("inter eth 5/" + str(i+10) +"/1."+str(j))
    child.expect("#")
    child.sendline("ip add 55."+str(i+10)+"."+str(j)+".1/24")
    child.expect("#")
    child.sendline("mac security profile test2")
    child.expect("#")
    child.sendline("mac security proxy patch eth 5/"+str(i+10)+"/1."+str(j+10))
    child.expect("#")
    child.sendline("inter eth 5/"+str(i+10)+"/1."+str(j+10))
    child.expect("#")
    child.sendline("vlan id "+str(j+count))
    child.expect("#")
    child.sendline("inter vx1")
    child.expect("#")
    child.sendline("vxlan vlan "+str(j+count)+" vni " + str(j+count))
    child.expect("#")
'''
count= 1160
for i in xrange(16,18):
  child.sendline("inter eth 5/" + str(i) +"/1")
  child.sendline("no sw")
  child.sendline("no shut")
  count = count+10
  for j in xrange(1,11):
    child.sendline("inter eth 5/" + str(i) +"/1."+str(j))
    child.expect("#")
    child.sendline("ip add 55."+str(i)+"."+str(j)+".1/24")
    child.expect("#")
    child.sendline("mac security profile test2")
    child.expect("#")
    child.sendline("mac security proxy patch eth 5/"+str(i)+"/1."+str(j+10))
    child.expect("#")
    child.sendline("inter eth 5/"+str(i)+"/1."+str(j+10))
    child.expect("#")
    child.sendline("vlan id "+str(j+count))
    child.expect("#")
    child.sendline("inter vx1")
    child.expect("#")
    child.sendline("vxlan vlan "+str(j+count)+" vni " + str(j+count))
    child.expect("#")
'''
count= 2990
for i in xrange(19,21):
  child.sendline("inter eth 5/" + str(i) +"/1")
  child.sendline("no sw")
  child.sendline("no shut")
  count = count+10
  for j in xrange(1,11):
    child.sendline("inter eth 5/" + str(i) +"/1."+str(j))
    child.expect("#")
    child.sendline("ip add 55."+str(i)+"."+str(j)+".1/24")
    child.expect("#")
    child.sendline("mac security profile test2")
    child.expect("#")
    child.sendline("mac security proxy patch eth 5/"+str(i)+"/1."+str(j+10))
    child.expect("#")
    child.sendline("inter eth 5/"+str(i)+"/1."+str(j+10))
    child.expect("#")
    child.sendline("vlan id "+str(j+count))
    child.expect("#")
    child.sendline("inter vx1")
    child.expect("#")
    child.sendline("vxlan vlan "+str(j+count)+" vni " + str(j+count))
    child.expect("#")
count= 3010
for i in xrange(21,26):
  child.sendline("inter eth 5/" + str(i) +"/1")
  child.sendline("no sw")
  child.sendline("no shut")
  count = count+10
  for j in xrange(1,11):
    child.sendline("inter eth 5/" + str(i) +"/1."+str(j))
    child.expect("#")
    child.sendline("ip add 55."+str(i)+"."+str(j)+".1/24")
    child.expect("#")
    child.sendline("mac security profile test2")
    child.expect("#")
    child.sendline("mac security proxy patch eth 5/"+str(i)+"/1."+str(j+10))
    child.expect("#")
    child.sendline("inter eth 5/"+str(i)+"/1."+str(j+10))
    child.expect("#")
    child.sendline("vlan id "+str(j+count))
    child.expect("#")
    child.sendline("inter vx1")
    child.expect("#")
    child.sendline("vxlan vlan "+str(j+count)+" vni " + str(j+count))
    child.expect("#")


count= 3060
for i in xrange(27,31):
  child.sendline("inter eth 5/" + str(i) +"/1")
  child.sendline("no sw")
  child.sendline("no shut")
  count = count+10
  for j in xrange(1,11):
    child.sendline("inter eth 5/" + str(i) +"/1."+str(j))
    child.expect("#")
    child.sendline("ip add 55."+str(i)+"."+str(j)+".1/24")
    child.expect("#")
    child.sendline("mac security profile test2")
    child.expect("#")
    child.sendline("mac security proxy patch eth 5/"+str(i)+"/1."+str(j+10))
    child.expect("#")
    child.sendline("inter eth 5/"+str(i)+"/1."+str(j+10))
    child.expect("#")
    child.sendline("vlan id "+str(j+count))
    child.expect("#")
    child.sendline("inter vx1")
    child.expect("#")
    child.sendline("vxlan vlan "+str(j+count)+" vni " + str(j+count))
    child.expect("#")
'''

child.sendline('exit')
child.expect("#")
child.close()
