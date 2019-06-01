fin = open('teleport.in', 'r')
fout = open('teleport.out', 'w')
start, end, t1, t2 = map(int, fin.readline().split())


def abs(num):
    if num < 0:
        num *= -1
    return num


def between(sp, mp, ep):
    return sp <= mp <= ep or ep <= mp <= sp


if between(start, t1, end) and between(start, t2, end):
    result = abs(t1-start) + abs(t2-end)
    result = min(result, abs(end-start))
    result = min(result, abs(t2 - start) + abs(t1-end))
if between(t1, start, end) and between(start, end, t2):
    result = abs(t1 - start) + abs(t2 - end)
    result = min(result, abs(end-start))
if between(start, t1, end) and between(t1, end, t2):
    result = abs(end-start)
    result = min(result, abs(t1-start) + abs(t2-end))
if between(start, t2, end) and between(t1, end, t2):
    result = abs(end-start)
    result = min(result, abs(t2-start) + abs(t1-end))
if between(start, t2, end) and between(t1, start, t2):
    result = abs(end - start)
    result = min(result, abs(t1 - start) + abs(t2 - end))
if between(start, t1, end) and between(t1, start, t2):
    result = abs(end-start)
    result = min(result, abs(t2-start) + abs(t1-end))
if not(between(start, t1, end) or between(start, t2, end)):
    result = abs(end-start)
fout.write(str(result) + '\n')
