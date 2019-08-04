fin = open('art.in', 'r')
fout = open('art.out', 'w')
N = int(fin.readline().strip())
B = []
for i in range(N):
    B.append(list(fin.readline().strip()))
for i in range(N):
    for j in range(N):
        B[i][j]=int(B[i][j])


def colorappears(c):
    for x in range(N):
        for j in range(N):
            if B[x][j] == c:
                return True
    return False


def c1onc2(c1, c2):
    top = N
    bottom = 0
    left = N
    right = 0
    for x in range(N):
        for j in range(N):
            if B[x][j] == c2:
                top = min(top, x)
                bottom = max(bottom, x)
                left = min(left, j)
                right = max(right, j)
    for x in range(top, bottom+1):
        for y in range(left, right+1):
            if B[x][y] == c1:
                return True
    return False


ans = 0
for m in range(1, 10):
    if colorappears(m):
        first = True
        for n in range(1, 10):
            if m != n and colorappears(n) and c1onc2(m, n):
                first = False
        if first:
            ans += 1
fout.write(str(ans)+'\n')



