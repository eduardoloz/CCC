'''
nums = []

for i in range(8):
	nums.append(int(input()))

print(nums)
triplecount	= 0
for i in range(len(nums)-3):
	prevsum = nums[i] + nums[i + 1] + nums[i + 2]
	nextsum = nums[i + 1] + nums[i + 2] + nums[i + 3]
	if nextsum > prevsum:
		triplecount += 1
print(triplecount)
'''
nums= []
xcount = 0
ycount = 0

for i in range(6):
	
	print(instructions)
	'''
	if line[0] == "foward":
		xcount += 1
	if line[0] == "down":
		ycount -= 1
	if line[0] == "up":
		ycount += 1
'''
print(xcount * ycount)
