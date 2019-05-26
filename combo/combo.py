"""
ID: ericvpe4
LANG: PYTHON3
TASK: combo
"""
import sys
fin = open('combo.in', 'r')
fout = open('combo.out', 'w')
N = int(fin.readline().split()[0])
L1A, L1B, L1C = map(int, fin.readline().split())
L2A, L2B, L2C = map(int, fin.readline().split())
lockpos = []
for i in range(1,N+1):
    lockpos.append(i)
lockpos *= 3
combpos = []
if N==1:
    fout.write('1'+'\n')
    sys.exit(0)
for a in range(-2,3):
    for b in range(-2, 3):
        for c in range(-2, 3):
            combogen = str(lockpos[L1A+N-1+a])+' '+str(lockpos[L1B+N-1+b])+' '+str(lockpos[L1C+N-1+c])
            combpos.append(combogen)
for a in range(-2,3):
    for b in range(-2, 3):
        for c in range(-2, 3):
            combogen = str(lockpos[L2A+N-1+a])+' '+str(lockpos[L2B+N-1+b])+' '+str(lockpos[L2C+N-1+c])
            combpos.append(combogen)
fout.write(str(len(set(combpos)))+'\n')

