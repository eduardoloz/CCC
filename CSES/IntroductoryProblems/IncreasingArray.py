n = int(input())

nums = [int(x) for x in input().split()]
moves = 0

for i in range(n-1):
	if nums[i] > nums[i+1]:
		moves += (nums[i] - nums[i+1])
		nums[i+1] = nums[i]

print(moves)

