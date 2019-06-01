fin = open('measurement.in', 'r')
fout = open('measurement.out', 'w')
N = int(fin.readline().strip())


def keywithmaxval(d):
    v = list(d.values())
    k = list(d.keys())
    value = max(v)
    return [k[index] for index, val in enumerate(v) if val == value]


log = []
for X in range(N):
    lineX = fin.readline().split()
    log.append([int(lineX[0]), lineX[1], int(lineX[2])])
log = sorted(log)
production = {'Mildred': 7,
              'Bessie': 7,
              'Elsie': 7}
prev =[]
cnt =0
for r in log:
    oldPro = production
    production[r[1]] += r[2]
    winner = keywithmaxval(production)
    if winner != prev:
        cnt +=1
        prev = winner
fout.write(str(cnt)+'\n')