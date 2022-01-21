lines = int(input())

for i in range(lines):
	[x, y] = map(int, input().split())
	largest = max(x,y)
	current_square = largest * largest


	if largest % 2 != 0:
		
