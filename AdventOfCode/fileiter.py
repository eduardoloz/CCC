#while True:
#	try: 
#		curr = input()
#	except EOFError:
#		break


# with input()
def readlines():
	while True:
		try: 
			yield input()
		except EOFError:
			break

# for line in readlines():
# 	print(line)

# with standard input
import sys

 while True:
 	line = sys.stdin.readline()
 		if line is None: break
 	print(line)

while (line:=sys.stdin.readline()):
	print(line)