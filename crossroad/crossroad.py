fin = open('crossroad.in', 'r')
fout = open('crossroad.out', 'w')
N = int(fin.readline().strip())
pos = []
IDs = []
for x in range(N):
    pos.append(fin.readline().split())
    pos[x][0], pos[x][1] = int(pos[x][0]), int(pos[x][1])
    IDs.append(pos[x][0])
IDs = list(set(IDs))
count = 0
for a in IDs:
    spec = []
    for b in pos:
        if b[0] == a:
            spec.append(b[1])
    print(a,spec)
    for c in range(len(spec)-1):
        if spec[c] != spec[c+1]:
            count += 1
            print(a, b, c, spec, count)
fout.write(str(count)+'\n')

