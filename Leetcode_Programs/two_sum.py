'''

Given an unsorted integer array, find a pair with the given sum in it.

• Each input can have multiple solutions. The output should match with either one of them.

Input : nums[] = [8, 7, 2, 5, 3, 1], target = 10
Output: (8, 2) or (7, 3)

• The solution can return pair in any order. If no pair with the given sum exists, the solution should return an empty tuple.

Input : nums[] = [5, 2, 6, 8, 1, 9], target = 12
Output: ()

'''


def findPair(nums: [], target: int):
	l1=[]
	for i in range(0,len(nums)):
		for j in range(i+1,len(nums)):
			if nums[i] + nums[j] == target:
				l1.append((nums[i],nums[j]))
	print(l1)

findPair ([8, 7, 2, 5, 3, 1], 10)
findPair ([5, 2, 6, 8, 1, 9], 12)