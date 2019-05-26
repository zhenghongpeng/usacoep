"""
ID: ericvpe4
LANG: PYTHON3
TASK: transform
"""
import sys
fin = open ('transform.in', 'r')
fout = open ('transform.out', 'w')
N = int(fin.readline().strip())
input = []
for i in range(N):
    input.append(list(fin.readline().strip()))
output = []
for i in range(N):
    output.append(list(fin.readline().strip()))
def rot90(input):
    tr = list(zip(*input[::-1]))
    return [list(row) for row in tr]
def refh(input):
    return [row[::-1] for row in input]

stage = input
for n in range(1,4):
    stage = rot90(stage)
    if stage == output:
        fout.write(str(n) + "\n")
        sys.exit(0)
if refh(input) == output:
    fout.write("4" + "\n")
    sys.exit(0)
stage = refh(input)
for n in range(1,4):
    stage = rot90(stage)
    if stage == output:
        fout.write(str(5) + "\n")
        sys.exit(0)
        break
if input == output:
    fout.write("6" + "\n")
    sys.exit(0)
fout.write("7" + "\n")

