n = int(input())

while (n != 1):
	print(n, end = " ")
	if (n % 2 == 0):
		n //= 2
	else:
		n = n * 3 + 1

print(n)

'''
To print in python3 without new line do:
print(blah, end = " "),
the end normally is automatically \n

if you have l = [1,2,3,4,5]
do print(*l)
to print 1 2 3 4 5 6
'''