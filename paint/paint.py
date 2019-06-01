fin = open ('paint.in', 'r')
fout = open ('paint.out', 'w')
a, b = map(int, fin.readline().split())
c, d = map(int, fin.readline().split())
if a <= b <= c <= d:
    len = d-c+b-a
if a <= c <= b <= d:
    len = d-a
if a <= c <= d <= b:
    len = b-a
if c <= a <= b <= d:
    len = d-c
if c <= a <= d <= b:
    len = b-c
if c <= d <= a <= b:
    len = b-a+d-c
fout.write(str(len)+'\n')
