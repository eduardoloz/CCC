dna = input()

max_len = 1

i = 0

while (i < len(dna) - 1):
	cur_len = 1
	while(i < len(dna) - 1 and dna[i] == dna[i+1]):
		cur_len += 1
		i += 1
	i += 1
	max_len = max(max_len, cur_len)

print(max_len)