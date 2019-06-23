import sys
fin = open ('factory.in', 'r')
fout = open ('factory.out', 'w')
N = int(fin.readline().strip())
startpt = []
endpt = []
for x in range(N-1):
    a, b = fin.readline().split()
    a, b = int(a), int(b)
    startpt.append(a)
    endpt.append(b)
print(startpt)
print(endpt)
pout = []
for x in endpt:
    if x not in startpt:
        pout.append(x)
if len(pout) == 0:
    fout.write('-1'+'\n')
pout = list(set(pout))
if len(pout) > 1:
    fout.write(str(-1)+'\n')
if len(pout) == 1:
    fout.write(str(pout[0])+'\n')
