import re

file = open("inputs/vraag5.txt", "r").readlines()
file = [f.replace("\n","") for f in file]

stack_data = file[:8]
stack_data = [i.replace("    ","-") for i in stack_data]
stacks = [[] for i in range(9)]

for i in reversed(stack_data):
    stack = 0
    for j in i:
        if (64 < ord(j) < 91):
            stacks[stack].append(j)
            stack += 1
        elif j == "-":
            stack += 1

moves = [re.findall(r'\d+',i) for i in file[-503:]]
moves = [[int(i) for i in j] for j in moves]

for move in moves:
    qty, origin, dest = move
    payload = stacks[origin-1][-qty:]
    
    for crate in payload:
        stacks[origin-1].pop()
        stacks[dest-1].append(crate)
for s in stacks:
    print(s[-1],end="")