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
'''
for i in xrange(1,256):
	child.sendline("ip route 20.1."+str(i)+".0/24  40.1."+str(i)+".1")
	child.expect("#")
        child.sendline("ipv6 route  20:1:"+hex(i)[2:]+"::0/64  40:1:"+hex(i)[2:]+"::1")
	child.expect("#")
child.sendline('exit')
child.expect("#")
'''
for i in xrange(256,512):
	child.sendline("ip route 20.2."+str(i-256)+".0/24  40.2."+str(i-256)+".1")
	child.expect("#")
        child.sendline("ipv6 route  20:1:"+hex(i)[2:]+"::0/64  40:1:"+hex(i)[2:]+"::1")
	child.expect("#")
child.sendline('exit')
child.expect("#")
'''
for i in xrange(512,768):
        vlanid=i+3023
	child.sendline("interface po10."+str(i))
	child.expect("#")
	child.sendline("vrf forwarding vrf1")
	child.expect("#")
	child.sendline("encapsulation dot1q vlan  "+str(vlanid))
	child.expect("#")
	child.sendline("ip address 40.3."+str(i-512)+".1/24")
	child.expect("#")
        child.sendline("ipv6 address 40:1:"+hex(i)[2:]+"::1/64")
	child.expect("#")
child.sendline('exit')
child.expect("#")
for i in xrange(768,1024):
        vlanid=i+3023
	child.sendline("interface po10."+str(i))
	child.expect("#")
	child.sendline("vrf forwarding vrf1")
	child.expect("#")
	child.sendline("encapsulation dot1q vlan  "+str(vlanid))
	child.expect("#")
	child.sendline("ip address 40.4."+str(i-768)+".1/24")
	child.expect("#")
        child.sendline("ipv6 address 40:1:"+hex(i)[2:]+"::1/64")
	child.expect("#")
child.sendline('exit')
child.expect("#")
'''
child.close()
