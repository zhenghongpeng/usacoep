"""
ID: ericvpe4
LANG: PYTHON3
TASK: crypt1
"""
fin = open('crypt1.in', 'r')
fout = open('crypt1.out', 'w')
digits = fin.readline().split()
digits = int(digits[0])
dlist = []
usable = list(map(int, fin.readline().split()))
count = 0
def valid(str):
    for char in str:
        if int(char) not in usable:
            return False
    return True
for a in range(digits):
    for b in range(digits):
        for c in range(digits):
            for d in range(digits):
                for e in range(digits):
                    aa = int(usable[a])
                    bb = int(usable[b])
                    cc = int(usable[c])
                    dd = int(usable[d])
                    ee = int(usable[e])
                    r1 = str(ee*(100*aa + 10*bb + cc))
                    r2 = str(dd*(100*aa + 10*bb + cc))
                    r3 = str((10*dd+ee)*(100*aa+10*bb+cc))
                    if len(r1)==3 and len(r2)==3 and len(r3)==4:
                        if valid(r1) and valid(r2) and valid(r3):
                            count += 1
fout.write(str(count) + '\n')




