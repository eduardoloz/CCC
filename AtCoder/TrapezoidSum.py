n = int(input())
sum = 0


for i in range(n):
	[x,y] = map(int, input().split())
	
	sum += (x + y) / 2 * (y - x + 1)
	#Partial sum formula 

print(int(sum))