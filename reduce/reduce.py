fin = open('reduce.in', 'r')
fout = open('reduce.out', 'w')
N = int(fin.readline().strip())
A = []
for i in range(N):
    A.append(fin.readline().split())
    A[i][0], A[i][1] = int(A[i][0]), int(A[i][1])

def awo(ii):
    bb = A.copy()
    bb.remove(bb[ii])
    bb = sorted(bb)
    minx = bb[0][0]
    maxx = bb[N-2][0]
    bb = sorted(bb, key=lambda x: x[1])
    miny = bb[0][1]
    maxy = bb[N-2][1]
    return (maxy - miny)*(maxx - minx)


A = sorted(A)
ans1 = min(awo(0), awo(-1))
A = sorted(A, key=lambda x: x[1])
ans2 = min(awo(0), awo(-1))
ans = min(ans1, ans2)
fout.write(str(ans)+'\n')