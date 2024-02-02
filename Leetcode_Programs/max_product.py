'''

Given an integer array, find a pair with the maximum product (result of multiply) in it.

Each input can have multiple solutions. The output should match with either one of them.

Input : [-10, -3, 5, 6, -2]
Output: (-10, -3) or (-3, -10) or (5, 6) or (6, 5)

Input : [-4, 3, 2, 7, -5]
Output: (3, 7) or (7, 3)

If no pair exists, the solution should return an empty tuple.

Input : [1]
Output: ()

'''

def findPair(nums: []):
	max=0
	pair=[]
	for i in range(len(nums)):
		for j in range(i+1, len(nums)):
			if max < (nums[i] * nums[j]):
				max = nums[i] * nums[j]
				pair.append((nums[i],nums[j]))
	return pair

print(findPair([-10, -3, 5, 6, -2]))
print(findPair([-4, 3, 2, 7, -5]))
print(findPair([1]))
