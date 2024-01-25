# Copyright (c) 2018 Arista Networks, Inc.  All rights reserved.
# Arista Networks, Inc. Confidential and Proprietary.

l = raw_input("Please enter numbers separated by space")
l = l.split( )
print l

s=0
for num in l:
 le=len(l)
 s=s+int(num)
a = int(s)/le 
print "sum is " + str(s)
print "avg is " + str(a)
