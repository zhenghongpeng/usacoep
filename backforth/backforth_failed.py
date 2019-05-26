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

def update(dic, key):
    if dic[key]>1:
        dic[key] -=1
    else:
        del dic[key]


valuelist = set()
for key in list(count1):
    a=key
    update(count1, key)
    count2[key] +=1
    for key in list(count2):
        b = key
        update(count2, key)
        count1[key] += 1
        for key in list(count1):
            c = key
            update(count1, key)
            count2[key] += 1
            for key in list(count2):
                d = key
                update(count2, key)
                count1[key] += 1
                valuelist.add((a,b,c,d))
                # print(a,b,c,d, 1000-a+b-c+d)
# print(valuelist)
answer = set([1000-a+b-c+d for a,b,c,d in valuelist])
print(answer)
fout.write(str(len(answer))+'\n')



