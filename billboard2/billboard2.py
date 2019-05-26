"""
ID: ericvpe4
LANG: PYTHON3
TASK: billboard
"""
fin = open('billboard.in', 'r')
fout = open('billboard.out', 'w')
x1, y1, x2, y2 = map(int, fin.readline().split())
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
    fout.write(str(((y2-y1)*(x2-x1))) + '\n')
if covcount == 1:
    fout.write(str(((y2-y1)*(x2-x1))) + '\n')
if covcount == 2:
    xL = max(x1, x3)
    xR = min(x2, x4)
    yL = max(y1, y3)
    yR = min(y2, y4)
    fout.write(str(((y2-y1)*(x2-x1)-(xR-xL)*(yR-yL))) + '\n')
if covcount == 4:
    fout.write('0' + '\n')
