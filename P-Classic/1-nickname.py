def nickname(name):
	largest = 0
	current = 0

	for i in range(len(name) - 1):
		if name[i] == name[i + 1]:
			current += 1
		else:
			current = 0

		largest = max(largest, current)
	print(largest)
	
nickname("aaabbbaaaabbb")
