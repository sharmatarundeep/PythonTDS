'''

Given a binary array, in-place sort it in linear time and constant space. The output should contain all zeroes, followed by all ones.

Input : [1, 0, 1, 0, 1, 0, 0, 1]
Output: [0, 0, 0, 0, 1, 1, 1, 1]

Input : [1, 1]
Output: [1, 1]

'''

'''Method 1 : using sort
def sortArray(nums:[]):
	nums.sort()
	return nums

print(sortArray([1, 0, 1, 0, 1, 0, 0, 1]))'''

#Method 2 : Using logic 2 for loops and compare elements and keep swaping as needeed
def sortArray(nums:[]):
	for i in range(0,len(nums)):
		for j in range (i+1,len(nums)):
			if nums[i] > nums[j]:
				nums[i],nums[j] = nums[j],nums[i]
	return nums

print(sortArray([1, 0, 1, 0, 1, 0, 0, 1]))
print(sortArray([1, 0, 2, 0, 9, 6, 11, 3]))