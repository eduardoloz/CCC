num = int(input())

for i in range(num):
	[a,b] = map(int, input().split())
	counter = 0
	while (a != 0):
		counter += 1
		if b > 1:
			a = a // b
		else:
			b += 1
	print(counter)
