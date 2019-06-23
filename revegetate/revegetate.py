import sys
fin = open ('revegetate.in', 'r')
fout = open ('revegetate.out', 'w')
N, M = map(int, fin.readline().split())
A, B, G = [], [], [0]*(N+1)
for x in range(M):
    y = fin.readline().split()
    y[0], y[1] = int(y[0]), int(y[1])
    A.append(y[0])
    B.append(y[1])
    if A[x] > B[x]:
        c = B[x]
        B[x] = A[x]
        A[x] = c
for i in range(1, N+1):
    for g in range(1, 5):
        b = 1
        for j in range(M):
            if B[j] == i and G[A[j]] == g:
                b = 0
        if b != 0:
            break
    G[i] = g
    fout.write(str(g))
fout.write('\n')
