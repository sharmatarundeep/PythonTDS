#!/usr/bin/python

import pexpect,timeit,datetime as dt
import sys,time,random
switch='lyv351'
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

for i in xrange(1,11):
        print i
        child.sendline("router ospf 1")
        child.expect("#")
	child.sendline("network 10.1."+str(i)+".1/24 area 0")
        child.expect("#")
        child.sendline("interface ether1/1."+str(i))
	child.expect("#")
	child.sendline("ipv6 ospf 1 area 0 ")
	child.expect("#")
child.sendline('exit')
child.expect("#")
'''
for i in xrange(256,512):
        print i
        child.sendline("router ospf 1")
        child.expect("#")
	child.sendline("network 24.2."+str(i-256)+".1/24 area 0")
        child.expect("#")
	child.sendline("interface ether24/1."+str(i))
	child.expect("#")
	child.sendline("ipv6 ospf 1 area 0 ")
	child.expect("#")
child.sendline('exit')
child.expect("#")

for i in xrange(512,768):
        print i
        child.sendline("router ospf 1")
        child.expect("#")
	child.sendline("network 24.3."+str(i-512)+".1/24 area 0")
        child.expect("#")
	child.sendline("interface ether24/1."+str(i))
	child.expect("#")
	child.sendline("ipv6 ospf 1 area 0 ")
	child.expect("#")
child.sendline('exit')
child.expect("#")

for i in xrange(768,1023):
        print i
        child.sendline("router ospf 1")
        child.expect("#")
	child.sendline("network 24.4."+str(i-768)+".1/24 area 0")
        child.expect("#")
	child.sendline("interface ether24/1."+str(i))
	child.expect("#")
	child.sendline("ipv6 ospf 1 area 0 ")
	child.expect("#")
child.sendline('exit')
child.expect("#")
'''
child.close()
