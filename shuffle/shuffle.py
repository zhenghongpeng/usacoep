fin = open('shuffle.in', 'r')
fout = open('shuffle.out', 'w')
N = int(fin.readline().split()[0])
shuffle = fin.readline().split()
IDs = fin.readline().split()
order = []
for x in range(1, N+1):
    order.append(x)


def reverse(sf, order):
    new = ['']*N
    for x in range(N):
        new[x] = shuffle[int(order[x])-1]
    return new


for i in range(3):
    order = reverse(shuffle, order)
print(order)
order2=['']*N
for x in range(len(order)):
    order2[x] = IDs[int(order[x])-1]
for x in order2:
    fout.write(x + '\n')
