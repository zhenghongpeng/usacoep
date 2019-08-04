fin = open('bcs.in', 'r')
fout = open('bcs.out', 'w')
N, M = map(int, fin.readline().split())
piece = [[] for _ in range(M+1)]
print(piece)

piece = [[] for _ in range(M+1)]
print(piece)
for y in range(M+1):
    # s=''
    for x in range(N):
        tmp = [c == '#' for c in list(fin.readline().strip())]
        piece[y].append(tmp)
print(piece[1])
print(piece[2])

def addpiece(p1, p2):
    p = [[False for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            p[i][j] = (p1[i][j] or p2[i][j])
    return p

def checkpiece(p1, p2):
    p = [[ False for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            p[i][j] = (p1[i][j] == p2[i][j])
    return all([all(row) for row in p])

pos ={}

# for y in range(1, M+1):
for y in range(1, M+1):
    pos[y] = []

    be = -1
    end = N
        tmp = [c == "#" for c in list(fin.readline().strip())]
        piece[y].append(tmp)
print(piece[1], piece[2])


    for r, row in enumerate(piece[y]):
        if any(row) == True and r < N:
            be = r
            break
    for r, row in enumerate(reversed(piece[y])):
        if any(row) == True and r < N:
            end = N-r
            break
def addpiece(p1, p2):
    p = [[False for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            p[i][j] = (p1[i][j] or p2[i][j])
    return p

    p = piece[y].copy()
    if be >0:
        for i in range(be):
            p.append(piece[y][0])
    if end < N:
        for i in range(end, N):
            p.insert(0, piece[y][-1])
    # pos[y] = p

    be = -1
    end = N
def checkpiece(p1, p2):
    p = [[ False for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            p[i][j]=(p1[i][j]==p2[i][j])
    return all([all(row) for row in p])

    # print(p)
    a = list(zip(*p))
    # print(k)
    # print(a)

    for r, row in enumerate(a):
        if any(row) == True and r < N:
            be = r
            break
    for r, row in enumerate(reversed(a)):
        if any(row) == True and r < N:
            end = N-r
            break
pos = {}

    p = a.copy()
    if be >0:
        for i in range(be):
            p.append(a[0])
    if end < N:
        for i in range(end, N):
            p.insert(0, a[-1])
    pos[y] = list(zip(*p))

    # print(be, end, pos[y])
# print(pos)

for y in pos:
    for z in pos:
        if y < z:
            can_a = []
            can_b = []
            a1 = pos[y].copy()
            tmp = [[False for j in range(N)] for i in range(N)]
            for i in range(0,len(a1)-N+1):
                for j in range(0,len(a1[0])-N+1):
                    tmp = [[a1[k+i][j+m] for m in range(N)]for k in range(N)]
                # print(tmp)
                    can_a.append(tmp)
            # print("can_a")
            # print(can_a)

            b1 = pos[z].copy()
            tmp = [[False for j in range(N)] for i in range(N)]
            for i in range(0,len(b1)-N+1):
                for j in range(0,len(b1[0])-N+1):
                    tmp = [[b1[k+i][j+m] for m in range(N)]for k in range(N)]
                # print(tmp)
                    can_b.append(tmp)
            # print("can_b")
            # print(can_b)

            for a in can_a:
                for b in can_b:
                    pieces = addpiece(a,b)
                    # print(f"compare {y}, {z}")
                    # print(a)
                    # print(b)
                    # print(pieces)
                    if checkpiece(piece[0], pieces):
                        fout.write(str(y)+" "+str(z)+"\n")
for y in range(1, M+1):
    pos[y]=[]
    be=-1
    end=N
    for r, row in enumerate(piece[y]):
        if any(row) == True and r<N:
            be=r
            break
    for r, row in enumerate(reversed(piece[y])):
        if any(row) == True and r<N:
            end=N-r
            break
    p=piece[y].copy()
    if be>0:
        for i in range(be):
            p.append(piece[y][0])
    if end<N:
        for i in range(end, N):
            p.insert(0, piece[y][-1])
    be=-1
    end=N
    a=list(zip(*p))
    for r, row in enumerate(a):
        if any(row) == True and r < N:
            be = r
            break
    for r, row in enumerate(reversed(a)):
        if any(row) == True and r < N:
            end = N - r
            break
    p=a.copy()
    if be>0:
        for i in range(be):
            p.append(a[0])
    if end<N:
        for i in range(end, N):
            p.insert(0, a[-1])
    pos[y]=list(zip(*p))
for y in pos:
    for z in pos:
        if y<z:
            can_a = []
            can_b = []
            a1=pos[y].copy()
            tmp=[[False for j in range(N)] for i in range(N)]
            for i in range(0, len(a1)-N+1):
                for j in range(0, len(a1[0])-N+1):
                    tmp=[[a1[k+i][j+m] for m in range(N)] for k in range(N)]
                    can_a.append(tmp)
            b1=pos[z].copy()
            tmp = [[False for j in range(N)] for i in range(N)]
            for i in range(0, len(b1) - N + 1):
                for j in range(0, len(b1[0]) - N + 1):
                    tmp=[[b1[k+i][j+m] for m in range(N)] for k in range(N)]
                    can_b.append(tmp)
            for a in can_a:
                for b in can_b:
                    pieces = addpiece(a, b)
                    if checkpiece(piece[0], pieces):
                        fout.write(str(y)+" "+str(z)+'\n')