fin = open('badmilk.in', 'r')
fout = open('badmilk.out', 'w')
N, M, D, S = map(int, fin.readline().split())
log = []
sicklog = []
for x in range(D):
    log.append(list(map(int, fin.readline().split())))
for x in range(S):
    sicklog.append(list(map(int, fin.readline().split())))
sick_milks = []
for p, t in sicklog:
    tmp =[]
    for l in log:
        if l[0] == p and l[2] < t:
            tmp.append(l[1])
    sick_milks.append(tmp)
# if len(sick_milks) > 1:
#     b_m = [set(sick_milks[0]).intersection(set(sick_milks[x])) for x in range(1, len(sick_milks))]
# else:
#     b_m = [sick_milks[0]]
# b_m = b_m[0]
# print(b_m)
# print(sick_milks)

start = set(sick_milks[0])
for l in sick_milks[1:]:
    start = start.intersection(set(l))
# print(start)
result = 0
for y in start:
    psick = []
    for x in log:
        if x[1] == y:
            psick.append(x[0])
    print(psick)

    psick = set(psick)
    if len(psick) > result:
        result = len(psick)
fout.write(str(result)+'\n')







