# Given an array of n integers, your task is to process q queries of the form: what is the minimum value in range [a,b]?

# Input

# The first input line has two integers n and q: the number of values and queries.

# The second line has n integers x1,x2,…,xn: the array values.

# Finally, there are q lines describing the queries. Each line has two integers a and b: what is the minimum value in range [a,b]?

# Output

# Print the result of each query.

# Constraints
# 1≤n,q≤2⋅105
# 1≤xi≤109
# 1≤a≤b≤n
# Example

# Input:
# 8 4
# 3 2 4 5 1 1 5 3
# 2 4
# 5 6
# 1 8
# 3 3

# Output:
# 2
# 1
# 1
# 4

n, q = map(int, input().split())
#print(n, q)
nums = list(map(int,input().split()))

pref = [0] * (n + 1)
for i in range(1, n + 1):
	pref[i] = pref[i-1] + nums[i-1]

for i in range(q):
	a, b = map(int, input().split(' '))
	difference = pref[b] - pref[a-1]
	print(difference)