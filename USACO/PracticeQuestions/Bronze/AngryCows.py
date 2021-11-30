# import sys

# #sys.stdin = open("angry.in", "r")
# #sys.stdout = open("angry.out", "w")

# N = int(input())

# arr = []

# for i in range(N):
# 	arr.append(int(input()))

# arr.sort()
# print(arr)

# #POTENTIAL STRATEGY
# greatest = 1
# #go through each "position" and simulate the explosions
# for i in range(N):
# 	left_count = 0
# 	right_count = 0
# 	total = 0
# 	#print("position is " + str(i))

# 	#stimulates left side
# 	#print("left side")
# 	for j in range(1,i):
# 		#print(j)
# 		if arr[i-j] < (arr[i] + j):
# 			left_count += 1
# 		else:
# 			break
# 	#stimulates right side
# 	#print("right side")
# 	for j in range(1,N-i):
# 		#print(j)
# 		if arr[i + j] < (arr[i] + j) :
# 			print("right side")
# 			right_count += 1
# 		else:
# 			break

# 	total = (right_count + left_count)
# 	print("total is: ")
# 	print(total)
# 	greatest = max(greatest, total + 1)

# print(greatest)

#---------------------------------------------------------------

import sys

#sys.stdin = open("angry.in" ,"r")
#sys.stdout = out("angry.out", "w")

n = int(input())

nums = []

for i in range(n):
	nums.append(int(input()))

nums.sort()


def max_radius(arr, i):
	#left
	left = 0
	while True:

	right = 0



	

