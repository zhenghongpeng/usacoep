fin = open('mowing.in', 'r')
fout = open('mowing.out', 'w')
N = int(fin.readline().strip())
dirdic = {"N": (-1, 0), "S": (1, 0), "E": (0, -1), "W": (0, 1)}
posx, posy = 1000, 1000
ctime = 0
mowing_map = x = [[-1 for i in range(2001)] for j in range(2001)]
result = 1001
log = []
for x in range(N):
    direc, steps = fin.readline().split()
    steps = int(steps)
    log.append((direc, steps))
for direc, steps in log:
    for step in range(1, steps + 1):
        posx += dirdic[direc][0]
        posy += dirdic[direc][1]
        ctime += 1
        if mowing_map[posx][posy] >= 0 and (ctime - mowing_map[posx][posy]) < result:
            result = ctime - mowing_map[posx][posy]
        else:
            mowing_map[posx][posy] = ctime
if result >= 1001:
    fout.write(str(-1) + '\n')
else:
    fout.write(str(result) + '\n')
