# A. Modulo Sequence
# time limit per test1 second
# memory limit per test256 megabytes
# inputstandard input
# outputstandard output
# You are given a single positive integer 𝑀. Construct an array of positive integers 𝑎1,…,𝑎𝑛 such that:

# 1≤𝑎𝑖≤𝑀 for all 1≤𝑖≤𝑛;
# 𝑎𝑖mod𝑎𝑖−1=𝑎𝑖−2 for all 3≤𝑖≤𝑛;
# The size of the array 𝑛 is largest possible.
# Input
# The first line of the input contains a single integer 𝑇 — the number of test cases (1≤𝑇≤10).

# Each test case is given as a line containing a single integer 𝑀 (1≤𝑀≤109).

# Output
# Output exactly two lines for each test case. The first line should contain a single integer 𝑛 — the size of your array.

# The second line should contain 𝑛 space-separated integers 𝑎1,…,𝑎𝑛 — the array itself.


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
	