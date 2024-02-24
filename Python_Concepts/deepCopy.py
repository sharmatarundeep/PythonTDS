# How to do deep copy so that the refence of copy variable is not same as the original variable 

# Regular copy 
list1 = [1,2,3,4]
list2 = list1 # copy list 1 to list 2
list2[1] = 5
print(list1) # both changed as this is regular copy
print(list2) # both changed as this is regular copy

# Deep copy 
import copy
list1 = [1,2,3,4]
list2 = copy.deepcopy(list1) # deep copy list 1 to list 2
list2[1] = 5
print(list1) # did not change when we changed list1
print(list2) # only change was here in list 2