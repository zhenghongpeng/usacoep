"""
ID: ericvpe4
LANG: PYTHON3
TASK: namenum
"""
fin = open ('namenum.in', 'r')
fout = open ('namenum.out', 'w')

cownum = fin.readline().strip()
trnum = {
    2 : "ABC",
    3 : "DEF",
    4 : "GHI",
    5 : "JKL",
    6 : "MNO",
    7 : "PRS",
    8 : "TUV",
    9 : "WXY"
}

def translate(ID):
    numlet = []
    for x in range(len(ID)):
        numlet.append(trnum[int(ID[x])])
    return numlet
perms = translate(cownum)
poss = []
with open('dict.txt', 'r') as f_dict:
    for line in f_dict:
        line = line.strip()
        state = ""
        for x in range(len(line)):
            if len(line) != len(perms):
                break
            if line[x] in perms[x]:
                state = state + line[x]
            if line == state:
                poss.append(line)
if len(poss) != 0:
    for x in poss:
        fout.write(x + "\n")
else:
    fout.write('NONE' + '\n')



