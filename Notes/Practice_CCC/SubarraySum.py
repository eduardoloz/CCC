#Subarray Sum

array = []
n = int(input())

# for i in range(n):
# 	array[:i] = int(input())


for i in range(n):
	array.append(int(input()))

mx = 0
sm = 0

for x in range(n):
	sm += array[i]

	if (sm <= 0):
		sm = 0:

	if (sm > mx):
		mx = sm


return mx
