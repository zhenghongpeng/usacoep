fin = open('measurement.in', 'r')
fout = open('measurement.out', 'w')
N = int(fin.readline().strip())
log = []
Mildred, Elsie, Bessie = 7, 7, 7
for X in range(N):
    lineX = fin.readline().split()
    log.append(lineX)
best = [Mildred, Elsie, Bessie]
counter = 0
for x in range(1,101):
    oldbest = best
    oldMildred = Mildred
    oldBessie = Bessie
    oldElsie = Elsie
    for i in range(N):
        if str(x) in log[i][0]:
            if log[i][1] == 'Mildred':
                Mildred += int(log[i][2])
            if log[i][1] == 'Elsie':
                Elsie += int(log[i][2])
            if log[i][1] == 'Bessie':
                Bessie += int(log[i][2])

    if max(Mildred, Elsie, Bessie) != max(oldbest):
        counter += 1
    if max(best) == max(oldbest):
        if (max(best) == Mildred) == (max(oldbest) == oldMildred):
            if (max(best) == Bessie) == (max(oldbest) == oldBessie):
                if (max(best) == Elsie) == (max(oldbest) == oldElsie):

        print(x, Elsie, Bessie, Mildred, counter)
print(counter)

