file = open('inputs/vraag4.txt','r')
getal1 = ''
getal2 = ''
getal3 = ''
getal4 = ''
counter = 0
counter2 = 0

for i in file:
	een = i.split(',')[0]
	twee = i.split(',')[1]
	for j in een:
		if j == '-':
			break
		else:
			getal1 = getal1 + j
	getal2 = een[1+len(getal1):]
	for j in twee:
		if j == '-':
			break
		else:
			getal3 = getal3 + j
	getal4 = twee[1+len(getal3):].strip()
	if ((int(getal1) >= int(getal3)) and (int(getal2) <= int(getal4))) or ((int(getal3) >= int(getal1)) and (int(getal4) <= int(getal2))):
		counter = counter + 1
	if ((int(getal1) >= int(getal4)) and (int(getal2) <= int(getal3))) or ((int(getal4) >= int(getal1)) and (int(getal3) <= int(getal2))):
		counter2 = counter2 + 1
	getal1 = ''
	getal2 = ''
	getal3 = ''
	getal4 = ''
print("Deel1: " + str(counter))
print("Deel2: " + str(counter2))