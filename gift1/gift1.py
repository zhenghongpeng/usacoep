"""
ID: ericvpe4
LANG: PYTHON3
TASK: gift1
"""
fin = open ('gift1.in', 'r')
fout = open ('gift1.out', 'w')
NP = int(fin.readline())
moneytable = {}
for i in range(NP):
    moneytable[fin.readline().strip()]=0
for i in range(NP):
    giver=fin.readline().strip()
    total, NR = map(int, fin.readline().split())
    if NR != 0:
        moneytable[giver] -= total - total % NR
        for i in range(NR):
            reciever = fin.readline().strip()
            moneytable[reciever]+=total//NR
for name, amount in moneytable.items():
    fout.write (name + " " + str(amount) + "\n")
fout.close()