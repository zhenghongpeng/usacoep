fin = open('buckets.in', 'r')
fout = open('buckets.out', 'w')
map = []
for x in range(10):
    map.append(fin.readline().strip())
    map[x].split()
print(map)
for a in map:
    for b in a:
        if b == 'B':
            x1, y1 = map.index(a), map[map.index(a)].index(b)
for a in map:
    for b in a:
        if b == 'L':
            x2, y2 = map.index(a), map[map.index(a)].index(b)
for a in map:
    for b in a:
        if b == 'R':
            xR, yR = map.index(a), map[map.index(a)].index(b)
if (x1 == xR == x2 and (y1 < yR < y2 or y2 < yR < y1))or y1 == yR == y2 and (x1 < xR < x2 or x2 < xR < x1):
    fout.write(str(abs(int(x1)-int(x2))+abs(int(y1)-int(y2))+1)+'\n')
else:
    fout.write(str(abs(int(x1) - int(x2)) + abs(int(y1) - int(y2))-1) + '\n')