fin = open('speeding.in', 'r')
fout = open('speeding.out', 'w')
N, M = map(int, fin.readline().split())
roads = []
cow = []
begin = 0
for x in range(N):
    roads.append(fin.readline().split())
    roads[x].append(begin+1)
    for i in range(2):
        roads[x][i] = int(roads[x][i])
    roads[x][0] += begin
    begin = int(roads[x][0])
begin = 0
for x in range(M):
    cow.append(fin.readline().split())
    cow[x].append(begin+1)
    for i in range(2):
        cow[x][i] = int(cow[x][i])
    cow[x][0] += begin
    begin = int(cow[x][0])


def between(a, b, c):
    return a <= b <= c or c <= b <= a


over = 0
for mile in range(1, 101):
    for x in range(N):
        for i in range(M):
            if between(roads[x][0], mile, roads[x][2]):
                if between(cow[i][0], mile, cow[i][2]):
                    over = max(over, cow[i][1]-roads[x][1])



fout.write(str(over)+'\n')