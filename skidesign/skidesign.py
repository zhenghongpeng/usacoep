"""
ID: ericvpe4
LANG: PYTHON3
TASK: skidesign
"""
fin = open('skidesign.in', 'r')
fout = open('skidesign.out', 'w')
N = int(fin.readline().strip())
heights = []
for hill in range(N):
    height = fin.readline().strip()
    heights.append(int(height))
heights = sorted(heights)
prices = []
for s in range(heights[0], heights[-1]-17):
    e = s+17
    p = 0
    for h in heights:
        if h < s:
            p += (h-s)**2
        elif h > e:
            p += (h-e)**2
    prices.append(p)
fout.write(str(min(prices) if prices else '0') + '\n')
