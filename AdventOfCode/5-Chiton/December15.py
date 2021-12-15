raw = open("in.txt", "r").read()

raw = raw.split("\n")

def blue(s):
	arr = []
	for pos in s:
		arr.append(int(pos))
	return arr
chitons = []

for line in raw:
	chitons.append(blue(line))


cp = [0, 0]
fp = [len(chitons[0]), len(chitons)]

print(fp)

while ((cp[0] != fp[0] - 1) and (cp[1] != fp[1])):
	if (chitons[cp[0] + 1, cp[1]] < chitons[cp[0], cp[1] + 1]):
		cp 

print(chitons)