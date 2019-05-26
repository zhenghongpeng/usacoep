"""
ID: ericvpe4
LANG: PYTHON2
TASK: ride
"""
fin = open ('ride.in', 'r')
fout = open ('ride.out', 'w')
comet = fin.readline().strip()
group = fin.readline().strip()
comprod = 1
for i in range(len(comet)):
    comprod = comprod*(ord(comet[i])-ord('A')+1)
groprod=1
for i in range(len(group)):
    groprod = groprod*(ord(group[i])-ord('A')+1)
if comprod % 47 == groprod % 47:
    fout.write ('GO' + '\n')
else:
    fout.write ('STAY' + '\n')
fout.close()