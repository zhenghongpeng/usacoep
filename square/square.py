fin = open('square.in', 'r')
fout = open('square.out', 'w')
x1, y1, x2, y2 = map(int, fin.readline().split())
x3, y3, x4, y4 = map(int, fin.readline().split())
minx, miny, maxx, maxy = 0, 0, 0, 0
minx = min(x1, x2)
minx = min(minx, x3)
minx = min(minx, x4)
maxx = max(x1, x2)
maxx = max(maxx, x3)
maxx = max(maxx, x4)
miny = min(y1, y2)
miny = min(miny, y3)
miny = min(miny, y4)
maxy = max(y1, y2)
maxy = max(y3, maxy)
maxy = max(y4, maxy)
fout.write(str(max(maxx-minx, maxy-miny)**2)+'\n')