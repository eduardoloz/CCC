import sys

sys.stdin = open("moobuzz.in", "r")
sys.stdout = open("moobuzz.out", "w")

N = int(input())

cycle = (N // 8) * 15

count = 0
extra = 0

for i in range(15):
	if count == (N % 8):
		break
	if (i % 5 != 0 and i % 3 != 0): 
		count += 1
		extra = i



num = cycle + extra

if (N % 8 == 0):
	num -= 1

print(num)