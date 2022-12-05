file = open('inputs/vraag1.txt','r')
waarde = 0
hoogste = 0
lijst = []
for i in file:
	if (i.isspace()):
		lijst.append(waarde)
		waarde = 0
	else:
 
		waarde+= int(i)
som = sorted(lijst)[-3:]
uitkomst = som[0] + som[1] + som[2]
print(uitkomst)