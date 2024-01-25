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
while True:
    print "going to configure shaping"
    for i in xrange(2,49,2):
        print i
        child.sendline("inter eth 6/" + str(i) + "/1, 10/" + str(i) + "/1")
        #child.sendline("inter eth 6/" + str(i) + "/1")
        child.expect("#")
        child.sendline("shape rate " + str(92-i) + " percent")
        child.expect("#")    
        time.sleep(1)
    print "configured shaping"
    print "going to remove shaping"
    child.sendline("inter eth 6/1/1-6/48/1, 10/1/1-10/48/1 ")
    child.expect("#")
    child.sendline("no shape rate ")
    child.expect("#")
    print "removed shaping"
    time.sleep(1)
child.sendline('exit')
child.expect("#")
child.close()
