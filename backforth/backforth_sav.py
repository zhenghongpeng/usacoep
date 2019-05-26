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

def fri(milk, l1, l2):
    for i in range(len(l2)):
        m = l2[i]
        result[m+milk]=1
    print(result)

def thur(milk, l1, l2):
    for i in range(len(l1)):
        m = l1[i]
        new_b2 = l2.copy()
        new_b2.append(m)
        new_b1 = l1.copy()
        new_b1.remove(m)
        fri(milk - m, new_b1, new_b2)
def wed(milk, l1, l2):
    for i in range(len(l2)):
        m = l2[i]
        new_b2 = l2.copy()
        new_b2.remove(m)
        new_b1 = l1.copy()
        new_b1.append(m)
        print(new_b1, new_b2)
        thur(milk + m, new_b1, new_b2)
def tue(milk, l1, l2):
    for i in range(len(l1)):
        m = l1[i]
        new_b2 = l2.copy()
        new_b2.append(m)
        new_b1 = l1.copy()
        new_b1.remove(m)
        print(new_b1, new_b2)
        wed(milk - m, new_b1, new_b2)
print(l1,l2)
tue(1000, l1, l2)
# print(valuelist)
# answer = set([1000-a+b-c+d for a,b,c,d in valuelist])
# print(answer)
fout.write(str(len(result))+'\n')



