n = int(input())

def howmanytimes2(n):
	while True:
		if(n % 2 == 0):
			n /=  2
		else:
			return n

for i in range(n):
	num = int(input())
	if (num % 2 != 0):
		print ("YES")
	else:
		if howmanytimes2(num) == 1:
			print("NO")
		else:
			print("YES")