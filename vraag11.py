file = open("inputs/vraag11.txt").read()
lines = [x for x in file.split('\n')]

aapje = []
operatie = []
delen = []
juist = []
fout = []

for i in file.split("\n\n"):
    nummer, items, functie, test, true, false = i.split("\n")
    aapje.append([int(i) for i in items.split(":")[1].split(",")])
    woorden = functie.split()
    functie = "".join(woorden[-3:])
    operatie.append(lambda old,functie=functie:eval(functie))
    delen.append(int(test.split()[-1]))
    juist.append(int(true.split()[-1]))
    fout.append(int(false.split()[-1]))

begin = aapje

kgm = 1
for x in delen:
    kgm = (kgm*x)

for part in [1,2]:
    C = [0 for _ in range(len(aapje))]
    aapje = begin
    for t in range(20 if part==1 else 10000):
        for i in range(len(aapje)):
            for item in aapje[i]:
                C[i] += 1
                item = operatie[i](item)
                if part == 2:
                    item %= kgm
                if part == 1:
                    item = (item // 3)
                if item % delen[i] == 0:
                    aapje[juist[i]].append(item)
                else:
                    aapje[fout[i]].append(item)
            aapje[i] = []
    print(sorted(C)[-1] * sorted(C)[-2])