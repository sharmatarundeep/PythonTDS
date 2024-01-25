#!/usr/bin/python

import pexpect,timeit,datetime as dt
import sys,time,random
switch='bko124'
#switch='sr399'
#switch='ro157.cs1'

child = pexpect.spawn("ssh admin@"+switch,timeout=120)

child.expect("#")
child.sendline("enable")
child.expect("#")
child.sendline("term len 0")
child.expect("#")
child.sendline("conf t")
child.expect("#")
for i in xrange(1,256):
        vlanid=i+3023
	child.sendline("interface vlan "+str(vlanid))
	child.expect("#")
	child.sendline("ip address 40.1."+str(i)+".2/24")
	child.expect("#")
        child.sendline("ipv6 address 40:1:"+hex(i)[2:]+"::2/64")
	child.expect("#")
child.sendline('exit')
child.expect("#")

for i in xrange(256,512):
        vlanid=i+3023
	child.sendline("interface vlan "+str(vlanid))
	child.expect("#")
	child.sendline("ip address 40.2."+str(i-256)+".2/24")
	child.expect("#")
        child.sendline("ipv6 address 40:1:"+hex(i)[2:]+"::2/64")
	child.expect("#")
child.sendline('exit')
child.expect("#")

for i in xrange(512,768):
        vlanid=i+3023
	child.sendline("interface vlan "+str(vlanid))
	child.expect("#")
	child.sendline("ip address 40.3."+str(i-512)+".2/24")
	child.expect("#")
        child.sendline("ipv6 address 40:1:"+hex(i)[2:]+"::2/64")
	child.expect("#")
child.sendline('exit')
child.expect("#")
for i in xrange(768,1024):
        vlanid=i+3023
	child.sendline("interface vlan "+str(vlanid))
	child.expect("#")
	child.sendline("ip address 40.4."+str(i-768)+".2/24")
	child.expect("#")
        child.sendline("ipv6 address 40:1:"+hex(i)[2:]+"::2/64")
	child.expect("#")
child.sendline('exit')
child.expect("#")

child.close()
