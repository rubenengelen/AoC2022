file = open('inputs/vraag2.txt','r')
score = 0
for i in file:
	deel = i.split()
	if deel[1] == "X":
		if deel[0] == "A":
			score = score + 3
		elif deel[0] == "B":
			score = score + 1
		elif deel[0] == "C":
			score = score + 2
	elif deel[1] == "Y":
		score = score + 3
		if deel[0] == "A":
			score = score + 1
		elif deel[0] == "B":
			score = score + 2
		elif deel[0] == "C":
			score = score + 3
	elif deel[1] == "Z":
		score = score + 6
		if deel[0] == "A":
			score = score + 2
		elif deel[0] == "B":
			score = score + 3
		elif deel[0] == "C":
			score = score + 1
print(score)