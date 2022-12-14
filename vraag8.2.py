import numpy as np

path = "inputs/vraag8.txt"
with open(path) as p:
	file = p.read().splitlines()
totaal = []

for (rij, i) in zip(file, range(len(file))):
	file[i] = list(map(int, [*rij]))
	
file = np.array(file)

for (x, x_val) in zip(file, range(len(file))):
        for (y, y_val) in zip(x, range(len(x))):
            score = 0
            boom_score = 1
            for boom in reversed(file[:x_val, y_val]):
                if y > boom:
                    score = score + 1
                elif y <= boom:
                    score = score + 1
                    break
                else:
                    break
            boom_score = boom_score * score
 
            score = 0
            for boom in file[x_val, y_val + 1:]:
                if y > boom:
                    score = score + 1
                elif y <= boom:
                    score = score + 1
                    break
                else:
                    break
            boom_score = boom_score * score
 
            score = 0
            for boom in file[x_val + 1:, y_val]:
                if y > boom:
                    score = score + 1
                elif y <= boom:
                    score = score + 1
                    break
                else:
                    break
            boom_score = boom_score * score
 
            score = 0
            for boom in reversed(file[x_val, :y_val]):
                if y > boom:
                    score = score + 1
                elif y <= boom:
                    score = score + 1
                    break
                else:
                    break
            boom_score = boom_score * score
            totaal.append(boom_score)
totaal = max(totaal)

print(totaal)