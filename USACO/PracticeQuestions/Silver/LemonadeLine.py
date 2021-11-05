import sys

sys.stdin = open("lemonade.in", "r")
sys.stdout = open("lemonade.out", "w")

n = int(input())
A = [int(x) for x in input().split()]
A = sorted(A)
min = n
for i in range(n):
	if (A[n - i - 1] < i):
		min = i
		break

print(min)

