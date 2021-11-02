N = int(input())


A = [int(x) for x in input().split()]

B = [int(x) for x in input().split()]


mx = A[0]
sm = B[0]
for i in range(N):
	mx = max(mx, A[i])

for i in range(N):
	sm = min(sm, B[i])

if (sm - mx) < 0:
	print(0)
else:
	print(sm - mx + 1)