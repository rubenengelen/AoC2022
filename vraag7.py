file = open("inputs/vraag7.txt")
data = file.read().splitlines()
path = ""
files = dict()
dirs = dict()
totaal = 0
kleinste = 70000000
totaleGrootte=0

for i in data:
    if (i[0:4] == "$ cd") and (i[5:7] != ".."):
        path = path + i[5:] + "/"
        dirs[path] = 0
    if i[5:7] == "..":
        topDir = path.rfind("/")
        tweedeDir = path[:topDir].rfind("/")
        path = path[:tweedeDir+1]
    if i.split(" ")[0].isnumeric():
        file = path + i.split(" ")[1]
        files[file] = i.split(" ")[0]
        dirs[path] = dirs[path] + int(i.split(" ")[0])

for i in files:       
    totaleGrootte += int(files[i])
vrij = kleinste - totaleGrootte

for i in dirs:
    currentpath = i
    while len(currentpath) > 2:
        parent = currentpath[:currentpath[:currentpath.rfind("/")].rfind("/") + 1]
        dirs[parent] += dirs[i]
        currentpath = parent

for i in dirs:
    if dirs[i] < 100000:
        totaal = totaal + dirs[i]

    if (vrij + dirs[i]) > 30000000:
        if kleinste > dirs[i]:
            kleinste = dirs[i]

print(totaal)
print(kleinste)