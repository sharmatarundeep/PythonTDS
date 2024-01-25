# Copyright (c) 2018 Arista Networks, Inc.  All rights reserved.
# Arista Networks, Inc. Confidential and Proprietary.

#!/usr/bin/python

import pexpect,timeit,datetime as dt
import sys,time,random
switch='nfc351'

child = pexpect.spawn("ssh admin@"+switch,timeout=120)

child.expect(">")
child.sendline("enable")
child.expect("#")
child.sendline("term len 0")
child.expect("#")
child.sendline("conf t")
child.expect("#")
#for i in xrange(1,100000000000):
while True:
    r1 = random.randint(1,6)
    #r2 = random.randint(1,49)
    print r1
    child.sendline("agent SandFabric-Fabric" + str(r1)+ " terminate")
    #child.sendline("inter eth 6/" + str(r1) + "/1")
    child.expect("#")
 #   child.sendline("no sw")
  #  child.expect("#")
   # child.sendline("sw")
    #child.expect("#")
    time.sleep(30)

child.sendline('exit')
child.expect("#")
child.close()
