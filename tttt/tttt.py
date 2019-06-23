fin = open('tttt.in', 'r')
fout = open('tttt.out', 'w')
ttt = []
winners = []
for i in range(3):
    ttt.append(list(fin.readline().strip()))

def countwinnerX(ttt_map, w):
    count1 = 0
    winners = set()
    for x in range(3):
        if ttt_map[0][x] == ttt_map[1][x] == ttt_map[2][x]:
            if ttt_map[0][x] == w:
                return True
    for x in range(3):
        if ttt_map[x][0] == ttt_map[x][1] == ttt_map[x][2]:
            if ttt_map[x][0] == w:
                return True
    if ttt_map[0][0] == ttt_map[1][1] == ttt_map[2][2]:
        if ttt_map[0][0] == w:
            return True
    if ttt_map[0][2] == ttt_map[1][1] == ttt_map[2][0]:
        if ttt_map[0][2] == w:
            return True
    return False




used = []
for x in ttt[0]:
    used.append(x)
for x in ttt[1]:
    used.append(x)
for x in ttt[2]:
    used.append(x)
used = sorted(list(set(used)))

count1 = 0
for k in used:
    if countwinnerX(ttt, k):
        count1 +=1
fout.write(str(count1)+'\n')




count2 = 0
winner = set()

for k in used:
    for l in used:
        if used.index(k) != used.index(l):
            tmp = [['' for i in range(3)] for i in range(3)]
            for i in range(3):
                for j in range(3):
                    if ttt[i][j] == l:
                        tmp[i][j] = k
                    else:
                        tmp[i][j] = ttt[i][j]
            print(k, l, tmp, ttt)

            if (not countwinnerX(ttt, k)) and countwinnerX(tmp, k):
                print(k, l, tmp, ttt, "***")
                winner.add((min(k, l), max(k, l)))





# for x in used:
#     for y in used:
#         if x != y:
#             if ttt[0][0] == x or ttt[0][0] == y:
#                 if ttt[0][1] == x or ttt[0][1] == y:
#                     if ttt[0][2] == x or ttt[0][2] == y:
#                         count2 += 1
#             if ttt[1][0] == x or ttt[1][0] == y:
#                 if ttt[1][1] == x or ttt[1][1] == y:
#                     if ttt[1][2] == x or ttt[1][2] == y:
#                         count2 += 1
#             if ttt[2][0] == x or ttt[2][0] == y:
#                 if ttt[2][1] == x or ttt[2][1] == y:
#                     if ttt[2][2] == x or ttt[2][2] == y:
#                         count2 += 1
#             for b in range(3):
#                 if ttt[0][b] == x or ttt[0][b] == y:
#                     if ttt[1][b] == x or ttt[1][b] == y:
#                         if ttt[1][b] == x or ttt[1][b] == y:
#                             count2 += 1
#                 if ttt[0][0] == x or ttt[0][0] == y:
#                     if ttt[1][1] == x or ttt[1][1] == y:
#                         if ttt[2][2] == x or ttt[2][2] == y:
#                             count2 += 1
#                 if ttt[2][0] == x or ttt[2][0] == y:
#                     if ttt[1][1] == x or ttt[1][1] == y:
#                         if ttt[0][2] == x or ttt[0][2] == y:
#                             count2 += 1
fout.write(str(len(winner))+'\n')

