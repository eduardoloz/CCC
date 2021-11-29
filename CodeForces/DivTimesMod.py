n, k = map(int, input().split((" ")))

x = 0

potential_solutions = 0

x = k + n

while ((x // k) * (x % k) != n):
	x += 1

print(x) 

#Why is this hard :(
'''
	x // k * (x % k) == n
	
	x * (x % k) == n * k
'''
