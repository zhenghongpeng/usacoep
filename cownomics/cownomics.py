fin = open('cownomics.in', 'r')
fout = open('cownomics.out', 'w')
N, M = map(int, fin.readline().split())
spot = []
plain = []
for i in range(N):
    spot.append(fin.readline().strip())
for i in range(N):
    plain.append(fin.readline().strip())
ans = 0
for i in range(M):
    spotv = []
    plainv = []
    for j in range(N):
        spotv.append(spot[j][i])
    for j in range(N):
        plainv.append(plain[j][i])
    intersect = [x for x in spotv if x in plainv]
    if not intersect:
        ans += 1
fout.write(str(ans)+'\n')