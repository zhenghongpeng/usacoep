import sys
fin = open('pails.in', 'r')
fout = open('pails.out', 'w')
X, Y, M = map(int, fin.readline().split())
for x in range(M):
    for y in range(int((M -x)/X)+1):
        for z in range(int((M-x)/Y)+1):
            if X * y + Y * z == M - x:
                fout.write(str(M-x)+'\n')
                sys.exit(0)