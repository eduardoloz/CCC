# A. Modulo Sequence
# time limit per test1 second
# memory limit per test256 megabytes
# inputstandard input
# outputstandard output
# You are given a single positive integer ð. Construct an array of positive integers ð1,â¦,ðð such that:

# 1â¤ððâ¤ð for all 1â¤ðâ¤ð;
# ððmodððâ1=ððâ2 for all 3â¤ðâ¤ð;
# The size of the array ð is largest possible.
# Input
# The first line of the input contains a single integer ð â the number of test cases (1â¤ðâ¤10).

# Each test case is given as a line containing a single integer ð (1â¤ðâ¤109).

# Output
# Output exactly two lines for each test case. The first line should contain a single integer ð â the size of your array.

# The second line should contain ð space-separated integers ð1,â¦,ðð â the array itself.


M = int(input())

for x in range(M):
	fib = []
	x = 0
	line = ""

	maxnum = int(input())

	while(x < maxnum):
		if (x == 0):
			x += 1
			fib.append(1)
		elif (x == 1):
			fib.append(2)
			x += 1
		else:
			fib.append(fib[len(fib) - 1] + fib[len(fib) - 2])
			x += fib[len(fib) - 2]


	# for i in range(int(input()) - 1):
	# 	if (i == 0):
	# 		fib.append(1)		
	# 	elif (i == 1):
	# 		fib.append(2)
	# 	else:
	# 		fib.append(fib[i - 1] + fib[i - 2])
	# 		i += fib[i - 1]

	for i in range(len(fib)):
		line += str(fib[i]) + " "
	line += str(fib[len(fib) - 2])
	print(len(fib) + 1)
	print(line)
	