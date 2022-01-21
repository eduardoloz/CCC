length = int(input())

cows = input()

#print(cows)

valid_pics = 0


def legal(current):
	gCount = 0 
	hCount = 0
	for i in range(4):
		if current[i] == 'G':
			gCount += 1
		else:
			hCount += 1
	if gCount == 1 or hCount == 1:
		return False
	return True

for i in range(length-3):
	if legal([cows[i], cows[i + 1], cows[i + 2], cows[i + 3]]):
		valid_pics += (1 + length - (i + 4))

invalid_pics = 0

for i in range(length - 2):
	gCount = 0
	hCount = 0
	for j in range(i,length):
		if cows[j] == 'G':
			gCount += 1
		else:
			hCount += 1
		if hCount > 1 and gCount > 1:
			break;
		if gCount > 1 and hCount == 1:
			invalid_pics += 1
		if hCount > 1 and gCount == 1:
			invalid_pics += 1

print(invalid_pics)
