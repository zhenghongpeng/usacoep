fin = open('shuffle.in', 'r')
fout = open('shuffle.out', 'w')
N = int(fin.readline().split()[0])
shuffle = fin.readline().split()
IDs = fin.readline().split()


def reverseshuffle(IDlist):
    moveTo = [0]*(N+1)
    for x in range(1, N+1):
        destination = int(IDlist[i-1])
        moveTo[destination] = i
    return moveTo






sub = []
for i in range(N):
    sub.append(i+1)
a = reverseshuffle(shuffle)
b = reverseshuffle(a)
c = reverseshuffle(b)
result = []
for item in c:
    result.append(IDs[int(item)-1])
for item in result:
    fout.write(item + '\n')
