fin = open('notlast.in', 'r')
fout = open('notlast.out', 'w')
N = int(fin.readline().strip())
log = []
okay = []
fwf = {}
for i in range(N):
    log.append(fin.readline().split())
    log[i][1] = int(log[i][1])
for i in range(N):
    okay.append(log[i][0])
okay = list(set(okay))
for x in okay:
    fwf[x] = 0
for x in log:
    fwf[x[0]] += x[1]
ewfwef = []
for key in fwf:
for key in fwf:
    if fwf[key] == ewfwef[1]:
        fout.write(str(key)+'\n')
print(fwf, ewfwef)

