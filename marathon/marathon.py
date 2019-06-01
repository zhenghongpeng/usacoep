fin = open('marathon.in', 'r')
fout = open('marathon.out', 'w')
N = int(fin.readline().strip())
cp = []
ncp = []
result = -1
for x in range(N):
    cp.append(fin.readline().split())
    cp[x][0] = int(cp[x][0])
    cp[x][1] = int(cp[x][1])
for x in cp:
    dist = 0
    for y in cp:
        if x != y:
            ncp.append(y)
    for z in range(1, N-1):
        dist += abs(ncp[z][0] - ncp[z-1][0]) + abs(ncp[z][1] - ncp[z-1][1])
    if cp.index(x) != 0 and cp.index(x) != N-1:
        if result == -1:
            result = dist
        if result != -1:
            result = min(result, dist)
print(result)