fish = [1, 3, 4, 5, 1]

fish_count = [0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in range(len(fish)):
	fish_count[fish[i]] += 1
	
days = int(input())

def count_fish(a):
	count = 0
	for i in range(len(a)):
		count += a[i]
	return count

for i in range(days):
	print(fish_count)
	print(count_fish(fish_count))
	zero = fish_count[0]
	
	for i in range(len(fish_count)):
	
		fish_count[i] = fish_count[i + 1]
	fish_count[len(fish_count) - 1] = zero


