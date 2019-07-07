fin = open('blocks.in', 'r')
fout = open('blocks.out', 'w')


N = int(fin.readline().strip())
poss = []
for i in range(N):
    poss.append(fin.readline().split())


def countc(char, test_str):
    count = 0
    for i in test_str:
        if i == char:
            count = count + 1
    return count


def maxoccurences(i):
    counti = 0
    for x in range(N):
        counti += max(countc(i, poss[x][0]), countc(i, poss[x][1]))
    return counti


for i in range(97, 123):
    fout.write(str(maxoccurences(chr(i)))+'\n')
