import sys
fin = open('sleepy.in', 'r')
fout = open('sleepy.out', 'w')
N = int(fin.readline().split()[0])
ordering = fin.readline().split()
for i in range(1, N+1):
    for x in range(1, i):
        if int(ordering[N-x]) < int(ordering[N-i]):
            fout.write(str(N-i+1)+'\n')
            sys.exit(0)
fout.write('0'+'\n')
