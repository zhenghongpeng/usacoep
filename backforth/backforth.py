"""
ID: ericvpe4
LANG: PYTHON3
TASK: backforth
"""
from collections import Counter
fin = open('backforth.in', 'r')
fout = open('backforth.out', 'w')
b10, b11, b12, b13, b14, b15, b16, b17, b18, b19 = map(int, fin.readline().split())
b20, b21, b22, b23, b24, b25, b26, b27, b28, b29 = map(int, fin.readline().split())

poss = []
# for a in range(10):
l1 = [b10, b11, b12, b13, b14, b15, b16, b17, b18, b19]
count1 = Counter(l1)
l2 = [b20, b21, b22, b23, b24, b25, b26, b27, b28, b29]
count2 = Counter(l2)
result = {}


def Fri(milk, l1, l2):
    for i in range(len(l2)):
        m = l2[i]
        result[m + milk] = 1


def Thu(milk, l1, l2):
    for i in range(len(l1)):
        m = l1[i]
        new_b1 = l1.copy()
        new_b1.remove(m)
        new_b2 = l2.copy()
        new_b2.append(m)
        Fri(milk - m, new_b1, new_b2)


def Wed(milk, l1, l2):
    for i in range(len(l2)):
        m = l2[i]
        new_b1 = l1.copy()
        new_b1.append(m)
        new_b2 = l2.copy()
        new_b2.remove(m)
        Thu(milk + m, new_b1, new_b2)


def Tue(milk, l1, l2):
    for i in range(len(l1)):
        m = l1[i]
        new_b1 = l1.copy()
        new_b1.remove(m)
        new_b2 = l2.copy()
        new_b2.append(m)
        Wed(milk - m, new_b1, new_b2)


Tue(1000, l1, l2)
fout.write(str(len(result))+'\n')



