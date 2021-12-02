xcount = 0
ycount = 0

read = []

with open('December2.txt') as file:
	for line in file:
		line = line.split(" ")
		read.append(line)
		if line[0] == "forward":
			xcount += int(line[1])
		if line[0] == "down":
			ycount -= int(line[1])
		if line[0] == "up":
			ycount += int(line[1])
		print(xcount)
		print(ycount)

print(xcount * abs(ycount))

print(read)

position = 0
depth = 0
aim = 0

for i in range(len(read)):
	if read[i][0] == "forward":
		depth += (aim * int(read[i][1]))
		position += int(read[i][1])
	if read[i][0] == "down":
		aim += int(read[i][1])
	if read[i][0] == "up":
		aim -= int(read[i][1])
		
print(position * depth)
