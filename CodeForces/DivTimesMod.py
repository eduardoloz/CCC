n, k = map(int, input().split((" ")))

# Analysis
#The val (x % k) is a factor of n. So, n % (x % k) == 0 at some value

# (x // k) * (x % k) = n

#therefore, n * k // i = a factor


#CANNOT START AT K because then (x % k) = 0 - so k can't be factor of x


for i in range(k-1, 0, -1):
	if (n % i == 0):
		print(n // i * k + i)
		break


#while ((x // k) * (x % k) != n):
#	x += 1


#Why is this hard :(
'''
	x // k * (x % k) == n
	
	x * (x % k) == n * k
'''
