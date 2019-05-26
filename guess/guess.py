fin = open('guess.in', 'r')
fout = open('guess.out', 'w')
N = int(fin.readline().split()[0])
anitra = {}
result =0

def intersection(lst1, lst2):
    return len(set(lst1) & set(lst2))


for i in range(N):
    temporary = fin.readline().split()
    p = temporary[1]
    anitra[temporary[0]] = []
    for x in range(2, int(p)+2):
        anitra[temporary[0]].append(temporary[x])
tmp = 0
for ani1 in anitra:
    for ani2 in anitra:
        if ani1 != ani2:
            tmp = max(tmp, intersection(anitra[ani1], anitra[ani2]))
tmp += 1
fout.write(str(tmp)+'\n')




