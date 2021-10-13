n, k = map(int, input().split())

# while (n >= k):
# 	n -= k
# 	if n <= k:
# 		print("YES")
# 		break
# 	n -= k
# 	if n <= k:
# 		print("NO")

if n // k % 2 ==1:
	print("YES")
else:
	print("NO")
