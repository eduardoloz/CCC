# If three pairs of doubles, you go to "jail"
N = int(input()) #dice rolls

count = 0 
output = "No"

for i in range(N): 
  [d1, d2] = map(int, input().split())
  if d1 == d2:
    count += 1
  else:
    count = 0
  if count >= 3:
      output = "Yes"
      break

print(output)