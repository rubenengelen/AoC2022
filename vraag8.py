import numpy as np

path = "inputs/test.txt"
with open(path) as p:
	file = p.read().splitlines()
totaal = 0

for (rij, i) in zip(file, range(len(file))):
	file[i] = list(map(int, [*rij]))
	
file = np.array(file)

for (x, x_val) in zip(file, range(len(file))):
	for (y, y_val) in zip(x, range(len(x))):
		if (all(file[:x_val, y_val] < y) or all(file[x_val, y_val + 1:] < y) or all(file[x_val + 1:, y_val] < y) or all(file[x_val, :y_val] < y)):
			totaal = totaal + 1

print(totaal)