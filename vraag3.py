file = open('inputs/vraag3.txt','r')
uitkomst = 0
joepie = False
for i in file:
	eerste = i[:int(len(i)/2)]
	tweede = i[int(len(i)/2):]
	for j in eerste:
		for a in tweede:
			if joepie:
				break
			if j == a:
				joepie = True
				asci = ord(a)
				if(64 < asci < 91):
					value = (asci - 38)
				elif(96 < asci < 123):
					value = (asci - 96)
				uitkomst = uitkomst + value
	joepie = False
print(uitkomst)