fin = open('cow.in', 'r')
fout = open('cow.out', 'w')
N = int(fin.readline().strip())
s = fin.readline().strip()
numc, numco, numcow = 0, 0, 0
for x in range(N):
    if s[x] == 'C':
        numc += 1
    if s[x] == 'O':
        numco += numc
    if s[x] == 'W':
        numcow += numco
fout.write(str(numcow)+'\n')