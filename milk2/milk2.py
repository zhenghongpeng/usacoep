"""
ID: ericvpe4
LANG: PYTHON3
TASK: milk2
"""
fin = open ('milk2.in', 'r')
fout = open ('milk2.out', 'w')

N = int(fin.readline())
nodes = set()
for i in range(N):
    start, end = map(int, fin.readline().split())
    nodes.update(range(start, end))
s_min, s_max = min(nodes), max(nodes)
print(s_min, s_max)
print(nodes)
milked = []
for i in range(s_min, s_max+1):
    if i in nodes:
        milked.append("1")
    else:
        milked.append("0")
s = ''.join(milked)
max_1 = s.split("0")
max_0 = s.split("1")
uptime = len(max(max_1))
downtime = len(max(max_0))
if len(s) == max(max_1):
    downtime = 0
fout.write(str(uptime) + " " + str(downtime) +"\n")
