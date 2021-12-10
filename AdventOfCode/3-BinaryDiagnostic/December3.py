'''
nums = []
with open('test.txt') as file:
	for line in file:
		nums.append(int(line, 2))

highest = nums[0]
lowest = nums[0]

for i in range(len(nums)):
	highest = max(highest, nums[i])
	lowest = min(lowest, nums[i])

print(nums)

print(lowest)
print(highest)
print(lowest * highest)
'''
read = open('test.txt', "r")
read = read.read().split()

with open('test.txt') as file:

print(read)

string = ""
otherstring =""

for i in range(5):
	count1 = 0
	count0 = 0
	for j in range(12):
		if read[j][i] == "1":
			count1 += 1
		else:
			count0 += 1
	if count1 < count0:
		string += "0"
		otherstring += "1"
	else:
		string += "1"
		otherstring += "0"

print(string, otherstring)

print(int(string, 2) * int(otherstring, 2))

read2 = open("December3.txt")
read2 = read2.read().split()

oxygen = ""
co2 = ""

for i in range(12):
	count1_1 = 0
	count0_1 = 0
	for j in range(1000):
		#print(i,j)
		if read2[j][i] == "1":
			count1_1 += 1
		else:
			count0_1 += 1
	if count1_1 > count0_1:
		oxygen += "1"
		co2 += "0"
	else:
		oxygen += "0"
		co2 += "1"

print(oxygen)
print(co2)

currentvals = 0




