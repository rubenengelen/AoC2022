file = open('inputs/vraag1.txt','r')
waarde = 0
hoogste = 0
for i in file:
	if (i.isspace()):
		if (waarde>hoogste):
			hoogste = waarde
		waarde = 0
	else:
 
		waarde+= int(i)
print(hoogste)