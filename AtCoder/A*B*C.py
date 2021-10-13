k = int(input())
triples = 0

for a in range(1, k + 1):
	for b in range(1, k // a + 1):
		for c in range(1, k // (a * b) + 1):

				triples += 1

print(triples)