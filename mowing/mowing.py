fin = open('mowing.in', 'r')
fout = open('mowing.out', 'w')
N = int(fin.readline().strip())
dir_dic ={"N": (-1, 0), "S": (1, 0), "E": (0, -1), "W": (0, 1)}
pos_x, pos_y = 1000, 1000

curr_time = 0
mowing_map = x = [[-1 for i in range(2001)] for j in range(2001)]
answer = 1001
move_steps=[]
for x in range(N):
    dir, steps = fin.readline().split()
    steps = int(steps)
    move_steps.append((dir,steps))
for dir, steps in move_steps:
    for step in range(1, steps+1):
        pos_x +=dir_dic[dir][0]
        pos_y +=dir_dic[dir][1]
        curr_time += 1
        if mowing_map[pos_x][pos_y] >=0 and (curr_time - mowing_map[pos_x][pos_y]) < answer:
            answer = curr_time - mowing_map[pos_x][pos_y]
        else:
            mowing_map[pos_x][pos_y] = curr_time
if answer >=1001:
    fout.write(str(-1) + '\n')
else:
    fout.write(str(answer)+'\n')




