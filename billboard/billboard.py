fin = open('billboard.in', 'r')
fout = open('billboard.out', 'w')
x1, y1, x2, y2 = map(int, fin.readline().split())
a1, b1, a2, b2 = map(int, fin.readline().split())
x3, y3, x4, y4 = map(int, fin.readline().split())


def covered(xa, ya, xb, yb, xp, yp):
    return xa <= xp <= xb and ya <= yp <= yb


covcount = 0
if covered(x3, y3, x4, y4, x1, y1):
    covcount += 1
if covered(x3, y3, x4, y4, x1, y2):
    covcount += 1
if covered(x3, y3, x4, y4, x2, y1):
    covcount += 1
if covered(x3, y3, x4, y4, x2, y2):
    covcount += 1
if covcount == 0:
    if x3 <= x1 <= x4 <= x2:
        area1 = (y2 - y1) * (x2 - x1) - (y4 - y3) * (x4 - x1)
    if x1 <= x3 <= x2 <= x4:
        area1 = (y2 - y1) * (x2 - x1) - (y4 - y3) * (x2 - x3)
    if y3 <= y1 <= y4 <= y2:
        area1 = (y2 - y1) * (x2 - x1) - (y4 - y1) * (x4 - x3)
    if y1 <= y3 <= y2 <= y4:
        area1 = (y2 - y1) * (x2 - x1) - (y2 - y3) * (x4 - x3)
    if x1 <= x3 <= x4 <= x2 and y1 <= y3 <= y4 <= y2:
        area1 = 0
if covcount == 1:
    if covered(x3, y3, x4, y4, x1, y1):
        area1 = (y2 - y1) * (x2 - x1) - (y4 - y1) * (x4 - x1)
    if covered(x3, y3, x4, y4, x1, y2):
        area1 = (y2 - y1) * (x2 - x1) - (y2 - y3) * (x4 - x1)
    if covered(x3, y3, x4, y4, x2, y1):
        area1 = (y2 - y1) * (x2 - x1) - (y4 - y1) * (x2 - x3)
    if covered(x3, y3, x4, y4, x2, y2):
        area1 = (y2 - y1) * (x2 - x1) - (y3 - y2) * (x3 - x2)
if covcount == 2:
    if covered(x3, y3, x4, y4, x1, y1):
        if covered(x3, y3, x4, y4, x2, y1):
            area1 = (y2 - y1) * (x2 - x1) - (y4 - y1) * (x2 - x1)
        if covered(x3, y3, x4, y4, x1, y2):
            area1 = (y2 - y1) * (x2 - x1) - (y2 - y1) * (x4 - x1)
    if covered(x3, y3, x4, y4, x2, y2):
        if covered(x3, y3, x4, y4, x2, y1):
            area1 = (y2 - y1) * (x2 - x1) - (y2 - y1) * (x2 - x3)
        if covered(x3, y3, x4, y4, x1, y2):
            area1 = (y2 - y1) * (x2 - x1) - (x2 - x1) * (y2 - y3)
if covcount == 4:
    area1 = 0


covcount = 0
if covered(x3, y3, x4, y4, a1, b1):
    covcount += 1
if covered(x3, y3, x4, y4, a1, y2):
    covcount += 1
if covered(x3, y3, x4, y4, a2, b1):
    covcount += 1
if covered(x3, y3, x4, y4, a2, b2):
    covcount += 1
if covcount == 0:
    if x3 <= a1 <= x4 <= a2:
        area2 = (b2 - b1) * (a2 - a1) - (y4 - y3) * (x4 - a1)
    if a1 <= x3 <= a2 <= x4:
        area2 = (b2 - b1) * (a2 - a1) - (y4 - y3) * (a2 - x3)
    if y3 <= b1 <= y4 <= b2:
        area2 = (b2 - b1) * (a2 - a1) - (y4 - b1) * (x4 - x3)
    if b1 <= y3 <= b2 <= y4:
        area2 = (b2 - b1) * (a2 - a1) - (b2 - y3) * (x4 - x3)
    if a1 <= x3 <= x4 <= a2 and b1 <= y3 <= y4 <= b2:
        area2 = 0
if covcount == 1:
    if covered(x3, y3, x4, y4, a1, b1):
        area2 = (y2 - y1) * (x2 - x1) - (y4 - b1) * (x4 - a1)
    if covered(x3, y3, x4, y4, a1, b2):
        area2 = (y2 - y1) * (x2 - x1) - (b2 - y3) * (x4 - x1)
    if covered(x3, y3, x4, y4, a2, b1):
        area2 = (y2 - y1) * (x2 - x1) - (y4 - b1) * (a2 - x3)
    if covered(x3, y3, x4, y4, a2, b2):
        area2 = (y2 - y1) * (x2 - x1) - (y3 - b2) * (x3 - a2)
if covcount == 2:
    if covered(x3, y3, x4, y4, a1, b1):
        if covered(x3, y3, x4, y4, a2, b1):
            area2 = (b2 - b1) * (a2 - a1) - (y4 - b1) * (a2 - a1)
        if covered(x3, y3, x4, y4, a1, b2):
            area2 = (b2 - b1) * (a2 - a1) - (y2 - b1) * (x4 - a1)
    if covered(x3, y3, x4, y4, a2, b2):
        if covered(x3, y3, x4, y4, a2, b1):
            area2 = (b2 - b1) * (a2 - a1) - (b2 - b1) * (a2 - x3)
        if covered(x3, y3, x4, y4, a1, b2):
            area2 = (b2 - b1) * (a2 - a1) - (a2 - a1) * (b2 - y3)
if covcount == 4:
    area2 = 0
fout.write(str(area1 + area2)+'\n')
