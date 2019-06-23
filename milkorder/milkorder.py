import sys
fin = open('milkorder.in', 'r')
fout = open('milkorder.out', 'w')
N, M, K = map(int, fin.readline().split())
ga = []
order_cow = list(map(int, fin.readline().split()))
# for x in order:
#     x = int(x)
print(order_cow)
for x in range(K):
    ga.append(fin.readline().split())
    ga[x][0], ga[x][1] = int(ga[x][0]), int(ga[x][1])
ga = sorted(ga)
print(ga)


final = ['']*N
pos_cow_1 = N-1
for x in ga:
    final[x[1]-1] = x[0]
if 1 in final:
    fout.write(str(final.index('') + 1) + '\n')
    sys.exit(0)
for i in range(len(final)):
    if final[i] in order_cow:
        p = order_cow.index(final[i])
        print(p, final[i])
        for s in range(p,-1,-1):
            if final[i] == '':
                final[i] = order_cow[s]
            else:
                if order_cow[s] not in final:
                    final[len(final[0:i]) - 1 - final[0:i][::-1].index('')] = order_cow[s]
        for s in range(len(order_cow)-1,p,-1):
            if final[i] == '':
                final[i] = order_cow[s]
            else:
                if order_cow[s] not in final:
                    final[len(final)-1-final[::-1].index('')] = order_cow[s]




if 1 in final:
    fout.write(str(final.index(1) + 1) + '\n')
else:
    fout.write(str(final.index('') + 1) + '\n')






print(final)



