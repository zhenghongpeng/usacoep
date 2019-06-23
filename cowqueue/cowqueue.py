fin = open('cowqueue.in', 'r')
fout = open('cowqueue.out', 'w')
N = int(fin.readline().strip())
log = []
for x in range(N):
    log.append(fin.readline().split())
    log[x][0], log[x][1] = int(log[x][0]), int(log[x][1])
log = sorted(log)
print(log)
for x in range(len(log)):
    if x != 0 and log[x][0] <= log[x-1][0] + log[x-1][1]:
        log[x][0] = log[x-1][0] + log[x-1][1]
fout.write(str(log[-1][0]+log[-1][1])+'\n')
