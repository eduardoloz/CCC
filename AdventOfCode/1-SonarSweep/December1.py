nums = []

count = 0
current = 9999999

with open('December1.txt') as file:
	for line in file:
		nums.append(int(line))
		if int(line) > current:
			count += 1
			#print(int(line), current)
		current = int(line)
		
print(count)

triplecount = 0

for i in range(len(nums)-3):
	prevsum = nums[i] + nums[i + 1] + nums[i + 2]
	nextsum = nums[i + 1] + nums[i + 2] + nums[i + 3]
	if nextsum > prevsum:
		triplecount += 1
print(triplecount)



#current = int(input())

# while True:
# 		try: 
# 			if current < int(input()):
# 				count += 1
# 			print("worked")
# 		except:
# 			print("broke")
# 			break
