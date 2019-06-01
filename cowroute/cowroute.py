fin = open('cowroute.in', 'r')
fout = open('cowroute.out', 'w')
A, B, N = map(int, fin.readline().split())
cost = -1
for x in range(N):
    price, cities = map(int, fin.readline().split())
    route = fin.readline().split()
    if str(A) in route and str(B) in route and route.index(str(B)) > route.index(str(A)):
        if cost != -1:
            cost = min(cost, price)
        if cost == -1:
            cost = price
fout.write(str(cost)+'\n')