file = open('inputs/vraag6.txt')
lengte = 14

for i in file:
	for j in range(len(i)-lengte-1):
		marker = i[j:j+lengte]
		if len(set(marker)) == lengte:
			print(j+lengte)
			break