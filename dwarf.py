dwarf = []
total = 0
for i in range(9):
    a = int(input())
    dwarf.append(a)
    total += a
for t1 in range(len(dwarf)-1):
    for t2 in range(t1+1,len(dwarf)):
        if (dwarf[t1] + dwarf[t2]) == total - 100:
            r1 = dwarf[t1]
            r2 = dwarf[t2]
            dwarf.remove(r1)
            dwarf.remove(r2)
            break
        if(len(dwarf) == 7):
            break
dwarf.sort()

for g in dwarf:
    print(g)
