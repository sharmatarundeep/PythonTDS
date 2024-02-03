'''

Check if a given string can be derived from another string by circularly rotating it. The rotation can be in a clockwise or anti-clockwise rotation.

Input: X = 'ABCD', Y = 'DABC'
Output: True
Explanation: 'DABC' can be derived from 'ABCD' by right-rotating it by 1 unit

'''
'''
# Logic for circularly rotating
st1 = "ABCD"
st1 = st1[1:] + st1[0] # left rotate by 1
print (st1)'''

def check(X: str, Y: str):
	if len(X) != len(Y):
		print("False")
		return False
	for i in range(len(X)):
		X = X[1:] + X[0] # left rotate X by 1 
		if X == Y:
			print("True")
			break

check("ABCD", "DABC") # True
check("ABCD", "DABCA") # False
check("ABCD", "CDAB") # True