# Copyright (c) 2018 Arista Networks, Inc.  All rights reserved.
# Arista Networks, Inc. Confidential and Proprietary.

a=101
for i in range(1,a+1):
   if i%3==0 and i%5==0:
      print "SmartyPants"
   if i%3==0:
      print "Smarty"
   if i%5==0:
      print "Pants"
   else: 
     print i


