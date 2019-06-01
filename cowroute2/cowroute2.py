fin = open('cowroute.in', 'r')
fout = open('cowroute.out', 'w')
A, B, N = map(int, fin.readline().split())
cost = -1
pos = []
for x in range(N):
    price, cities = map(int, fin.readline().split())
    route = fin.readline().split()
    pos.append([price, cities, route])
    if str(A) in route and str(B) in route and route.index(str(B)) > route.index(str(A)):
        if cost != -1:
            cost = min(cost, price)
        if cost == -1:
            cost = price


def inter(s1, s2):
    returned = []
    for x in s1:
        if x in s2:
            returned.append(x)
    return returned


for x in pos:
    if str(A) in x[2]:
        for y in pos:
            if str(B) in y[2]:
                common = inter(x[2], y[2])
                for z in common:
                    if x[2].index(z) >= x[2].index(str(A)):
                        if y[2].index(str(B)) >= y[2].index(z):
                            cost = min(cost, int(x[0]) + int(y[0]))
                            break
fout.write(str(cost)+'\n')
