import sys
fin = open('taming.in', 'r')
fout = open('taming.out', 'w')
N = int(fin.readline().strip())
log = fin.readline().split()
for x in range(N):
    log[x] = int(log[x])
for x in range(N - 1):
    if 1 <= log[x + 1] <= log[x]:
        fout.write('-1' + '\n')
        sys.exit(0)
breakouts = ['']*N
for x in range(1, N+1):
    if log[x-1] != -1:
        breakouts[x-log[x-1]-1] = 1
        if log[x-1] != 0:
            for i in range(x-log[x-1], x):
                breakouts[i] = 0
breakouts[0] = 1
mindays = 0
for x in range(N):
    if breakouts[x] == 1:
        mindays += 1
maxdays = mindays
for x in range(N):
    if breakouts[x] == '':
        maxdays += 1
print(breakouts)
fout.write(str(mindays) + ' ' + str(maxdays) + '\n')

