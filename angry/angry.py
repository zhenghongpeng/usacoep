import sys
fin = open('angry.in', 'r')
fout = open('angry.out', 'w')
N = int(fin.readline().strip())
loc = []
for x in range(N):
    loc.append(int(fin.readline().strip()))
loc = sorted(loc)


def inside(x, i, li):
    inr = []
    for a in li:
        if i >= x - a > 0:
            inr.append(a)
        if i >= a - x > 0:
            inr.append(a)
    return inr


result = 0
for item in loc:
    explode = [x]
    rad = 1
    while True:
        ext = inside(item, rad, loc)
        if len(ext) == 0:
            break
        explode1 = explode
        explode = set(explode)
        ext = set(ext)
        explode.union(ext)
        explode = list(explode)
        if len(explode1) == len(explode):
            break
        ext = list(ext)
        rad += 1
        item = ext[0]
        if len(explode) == N:
            fout.write(str(N)+'\n')
            sys.exit(0)
    rad = 1
    while True:
        ext = inside(item, rad, loc)
        if len(ext) == 0:
            break
        explode1 = explode
        explode = set(explode)
        ext = set(ext)
        explode.union(ext)
        if len(explode1) == len(explode):
            break
        explode = list(explode)
        ext = list(ext)
        rad += 1
        item = ext[-1]
        if len(explode) == N:
            fout.write(str(N)+'\n')
            sys.exit(0)
    result = max(result, len(explode))
fout.write(str(result)+'\n')







