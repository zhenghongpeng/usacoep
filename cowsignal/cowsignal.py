fin = open('cowsignal.in', 'r')
fout = open('cowsignal.out', 'w')
A, B, N = map(int, fin.readline().split())
map = []
for i in range(A):
    map.append(list(fin.readline().strip()))
for i in map:
    for l in range(N):
        for j in range(B):
            for k in range(N):
                fout.write(str(i[j]))
        fout.write('\n')