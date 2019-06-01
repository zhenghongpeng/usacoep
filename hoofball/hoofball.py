fin = open('hoofball.in', 'r')
fout = open('hoofball.out', 'w')
N = int(fin.readline().strip())
loc = fin.readline().split()
passto = [0]*N
for x in range(N):
    loc[x] = int(loc[x])
loc = sorted(loc)


def nearest(tok, li):
    if tok == len(li)-1:
        return tok-1
    if tok == 0:
        return 1
    ld = li[tok]-li[tok-1]
    rd = li[tok+1]-li[tok]
    if ld <= rd:
        return tok-1
    return tok+1


count = 0
for i in range(N):
    passto[nearest(i, loc)] += 1
for i in range(N):
    if passto[i] == 0:
        count += 1
    # if (i < target(i) && target(target(i))==i && passto[i]==1 && passto[target(i)]==1)
    target = nearest(i, loc)
    print(target)
    if i < target and nearest(nearest(i, loc), loc)==i and passto[i]==1 and passto[nearest(i, loc)]==1:
        count += 1
fout.write(str(count)+'\n')
