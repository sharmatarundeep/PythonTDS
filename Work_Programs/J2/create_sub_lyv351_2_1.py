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
for i in xrange(1,256):
        vlanid=i+2000
	child.sendline("interface ether2/1."+str(i))
	child.expect("#")
	child.sendline("encapsulation dot1q vlan  "+str(vlanid))
	child.expect("#")
	child.sendline("ip address 30.1."+str(i)+".1/24")
	child.expect("#")
        child.sendline("ipv6 address 30:1:"+hex(i)[2:]+"::1/64")
	child.expect("#")
child.sendline('exit')
child.expect("#")

for i in xrange(256,512):
        vlanid=i+2000
	child.sendline("interface ether2/1."+str(i))
	child.expect("#")
	child.sendline("encapsulation dot1q vlan  "+str(vlanid))
	child.expect("#")
	child.sendline("ip address 30.2."+str(i-256)+".1/24")
	child.expect("#")
        child.sendline("ipv6 address 30:1:"+hex(i)[2:]+"::1/64")
	child.expect("#")
child.sendline('exit')
child.expect("#")

for i in xrange(512,768):
        vlanid=i+2000
	child.sendline("interface ether2/1."+str(i))
	child.expect("#")
	child.sendline("encapsulation dot1q vlan  "+str(vlanid))
	child.expect("#")
	child.sendline("ip address 30.3."+str(i-512)+".1/24")
	child.expect("#")
        child.sendline("ipv6 address 30:1:"+hex(i)[2:]+"::1/64")
	child.expect("#")
child.sendline('exit')
child.expect("#")
for i in xrange(768,1024):
        vlanid=i+2000
	child.sendline("interface ether2/1."+str(i))
	child.expect("#")
	child.sendline("encapsulation dot1q vlan  "+str(vlanid))
	child.expect("#")
	child.sendline("ip address 30.4."+str(i-768)+".1/24")
	child.expect("#")
        child.sendline("ipv6 address 30:1:"+hex(i)[2:]+"::1/64")
	child.expect("#")
child.sendline('exit')
child.expect("#")

child.close()
