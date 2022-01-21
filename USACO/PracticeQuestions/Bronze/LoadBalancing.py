number = int(input())

xcows = []
ycows = []

for i in range(number):
	current = input().split()
	xcows.append(int(current[0]))
	ycows.append(int(current[1]))

print(xcows)
print(ycows)


#Testing positions of line
xpos = 0
ypos = 0

while xpos < 