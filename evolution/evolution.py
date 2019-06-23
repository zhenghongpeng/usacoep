import sys
fin = open ('evolution.in', 'r')
fout = open ('evolution.out', 'w')
N = int(fin.readline().strip())
subpops = []
for x in range(N):
    temp = fin.readline().split()
    temp2 = [x for x in temp if temp.index(x) != 0]
    subpops.append(temp2)
traits = []
for x in subpops:
    for y in x:
        traits.append(y)
traits = list(set(traits))
for a in traits:
    for b in traits:
        if a != b:
            for x in subpops:
                for y in subpops:
                    for z in subpops:
                        if a in x and b in x and a in y and not b in y and not a in z and b in z:
                            fout.write('no\n')
                            sys.exit(0)
fout.write('yes\n')