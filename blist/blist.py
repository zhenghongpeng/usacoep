"""
ID: ericvpe4
LANG: PYTHON3
TASK: blist
"""
fin = open('blist.in', 'r')
fout = open('blist.out', 'w')
s = []
t = []
b = []
N = int(fin.readline().split()[0])
for i in range(N):
    a, b1, c = map(int, fin.readline().split())
    s.append(a)
    t.append(b1)
    b.append(c)
needed = 0
for i in range(min(s), max(t)+1):
    current = 0
    for x in range(N):
        if s[x] <= i <= t[x]:
            current += b[x]
    needed = max(needed, current)
fout.write(str(needed) + '\n')
