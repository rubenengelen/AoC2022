file = open("inputs/vraag10.txt")
counter = 1
x = 1
total = 0
total1 = 0
total2 = 0
total3 = 0
total4 = 0
total5 = 0
total6 = 0

for i in file:
	if i[0:1] == 'a':
		counter += 2
		x += int(i[5:])
	elif i[0:1] == 'n':
		counter += 1
	if counter == 20:
		total1 = x*20
	elif counter == 59:
		total2 = x*60
	elif counter == 99:
		total3 = x*100
	elif counter == 139:
		total4 = x*140
	elif counter == 180:
		total5 = x*180
	elif counter == 219:
		total6 = x*220
total = total1 + total2 + total3 + total4 + total5 + total6
print(total)
