fin = open('badmilk.in', 'r')
fout = open('badmilk.out', 'w')
N, M, D, S = map(int, fin.readline().split())
log = []
sicklog = []
for x in range(D):
    log.append(fin.readline().split())
for x in range(S):
    sicklog.append(fin.readline().split())
print(log, sicklog)
#for x in range(1, M+1):

