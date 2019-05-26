fin = open('shell.in', 'r')
fout = open('shell.out', 'w')
N = int(fin.readline().split()[0])
swaps = []
for i in range(N):
    swaps.append(fin.readline().split())
maximized = 0
for i in range(1,4):
    if i == 1:
        current = [1, 0, 0]
    if i == 2:
        current = [0, 1, 0]
    if i == 3:
        current = [0, 0, 1]
    now = 0
    for x in range(N):
        a = swaps[x][0]
        b = swaps[x][1]
        sub = current[int(a)-1]
        current[int(a)-1] = current[int(b)-1]
        current[int(b)-1] = sub
        if current[int(swaps[x][2])-1] == 1:
            now += 1
    maximized = max(maximized, now)
fout.write(str(maximized) + '\n')
