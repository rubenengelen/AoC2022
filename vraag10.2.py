x = 1
cycle = 0
pixels = list("." * 40 * 6)

with open("inputs/vraag10.txt") as file:
	lines = [line.rstrip() for line in file.readlines()]

def update(x, cycle, pixels):
	positie = (cycle) % 40
	if positie in {x-1, x, x+1}:
		pixels[cycle] = "#"
		
for line in lines:
	line = line.split()
	
	if line[0] == "noop":
		update(x, cycle, pixels)
		cycle += 1
		
	elif line[0] == "addx":
		update(x, cycle, pixels)
		cycle += 1
		update(x, cycle, pixels)
		cycle += 1

		x += int(line[1])
			
for i in range(0, 201, 40):
	print("".join(pixels[i: i + 40]))