fin = open('notlast.in', 'r')
fout = open('notlast.out', 'w')
N = fin.readline().strip()
log = []
okay = []
for i in range(N):
    log.append(fin.readline().split())
    log[i][1] = int(log[i][1])
for i in range(N):
    okay.append(log[i][1])
okay = sorted(okay)
