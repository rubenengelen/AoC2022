file = open('inputs/vraag3.txt','r')
joepie = False
uitkomst = 0

for i in file:
	een = i
	twee = file.readline()
	drie = file.readline()
	for a in een:
		for b in twee:
			for c in drie:
				if joepie:
					break
				if a == b and b == c and a == c:
					asci = ord(a)
					if(64 < asci < 91):
						value = (asci - 38)
					elif(96 < asci < 123):
						value = (asci - 96)
					print(a)
					print(value)
					uitkomst = uitkomst + value
					joepie = True
	joepie = False
print(uitkomst)