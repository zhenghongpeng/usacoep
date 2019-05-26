"""
ID: ericvpe4
LANG: PYTHON3
TASK: mixmilk
"""
fin = open('mixmilk.in', 'r')
fout = open('mixmilk.out', 'w')
c1, m1 = map(int, fin.readline().split())
c2, m2 = map(int, fin.readline().split())
c3, m3 = map(int, fin.readline().split())
for i in range(1,101):
    mod2 = i % 3
    if mod2 == 1:
        m2a = min(m1 + m2, c2)
        m1a = max(0, m1 + m2 - c2)
        m2 = m2a
        m1 = m1a
    if mod2 == 2:
        m3a = min(m2 + m3, c3)
        m2a = max(0, m2 + m3 - c3)
        m3 = m3a
        m2 = m2a
    if mod2 == 0:
        m1a = min(m3 + m1, c1)
        m3a = max(0, m3 + m1 - c1)
        m1 = m1a
        m3 = m3a
fout.write(str(m1)+'\n'+str(m2)+'\n'+str(m3)+'\n')
