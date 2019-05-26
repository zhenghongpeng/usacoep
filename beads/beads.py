"""
ID: ericvpe4
LANG: PYTHON3
TASK: beads
"""
fin = open ('beads.in', 'r')
fout = open ('beads.out', 'w')
N = int(fin.readline().strip())
necklace = fin.readline().strip()
necklace = necklace * 3
#s is an extended string in necklace, a is direction to be extended
def ifExtend(c, s):
    for i in range(len(s)):
        if s[i] == "w":
            continue
        if s[i] == "r":
            if c != "b":
                return True
        else:
            if c != "r":
                return True
    if s == "":
        return True
    return False
def ifValid(s):
    return not ('r' in s and 'b' in s)

max_ = 0
for i in range(N, 2*N):
    left = ""
    right = ""
    p = i-1
    for m in range(p, -1,-1):
        # if ifExtend(necklace[m], left):
        if ifValid(left+necklace[m]):
            left += necklace[m]
        else:
            break
    p = i
    for m in range(p, 3*N):
        if ifExtend(necklace[m], right):
        # if ifValid(right+necklace[m]):
            right += necklace[m]
        else:
            break
    max_ = min(max(max_, len(left)+len(right)),N)
    # print(i, "l", left, "r", right, max_)
fout.write(str(max_)+"\n")


