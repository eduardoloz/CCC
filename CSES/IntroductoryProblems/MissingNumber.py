n = int(input())

expected_sum = n * (n + 1) // 2
observed_sum = 0

for nums in input().split():
	observed_sum += int(nums)

print(expected_sum - observed_sum)