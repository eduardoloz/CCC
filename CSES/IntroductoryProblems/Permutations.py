n = int(input())

#nums = []

if (n == 1):
	print("1")

elif (n < 4):
	print("NO SOLUTION")

else:
	for i in range(1, n // 2 + 1):
		print(i * 2, end = " ")
	for i in range(n // 2, n):
		print(1 + 2 * (i - n // 2), end = " ")



			

#print(" ".join(str(x) for x in nums))

