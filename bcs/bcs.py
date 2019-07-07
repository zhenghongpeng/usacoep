import sys
fin = open('bcs.in', 'r')
fout = open('bcs.out', 'w')
N, M = map(int, fin.readline().split())
piece = []
for y in range(M+1):
    s=''
    for x in range(N):
        # piece[y].append(list(fin.readline().strip()))
        s += ''.join(fin.readline().strip())

    piece.append(s.count('#'))
# print(piece)

for k, e1 in enumerate(piece[1:]):
    rem = piece[0] - e1
    if rem in piece[k+1:]:
        # print(k+1, str(piece[k+2:].index(rem)+k+3) )
        print(str(k+1)+' '+ str(piece[k+2:].index(rem)+k+3))

        fout.write(str(k+1)+' '+ str(piece[k+2:].index(rem)+k+2)+'\n')
        sys.exit(0)






