"""
ID: ericvpe4
LANG: PYTHON3
TASK: barn1
"""
fin = open('barn1.in', 'r')
fout = open('barn1.out', 'w')
M, S, C = map(int, fin.readline().split())
occ = []
for i in range(C):
    x = fin.readline().split()[0]
    occ.append(int(x))
occ = sorted(occ)
print(occ)
gaps = []
for x in range(1, C):
    gaps.append(int(occ[x])-int(occ[x-1]))
gaps = sorted(gaps, reverse=True)
print(gaps)
minimized = int(occ[-1])-int(occ[0])+1
if M <= C:
    for i in range(M-1):
        minimized = minimized-gaps[i]+1
else:
    fout.write(str(C) + "\n")
if M <= C:
    fout.write(str(minimized) + "\n")
