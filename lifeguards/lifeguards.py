fin = open('lifeguards.in', 'r')
fout = open('lifeguards.out', 'w')
N = int(fin.readline().strip())
times = []
for x in range(N):
    times.append(fin.readline().split())
    times[x][0], times[x][1] = int(times[x][0]), int(times[x][1])
times = sorted(times)
print(times)
result = 0
#
#
# def hours_overlap(a, b):
#     count = a[1] + b[1] - a[0] - b[0]
#     if a[0] < b[0]:
#         if a[1] > b[0]:
#             count -= a[1] - b[0]
#     if a[0] > b[0]:
#         if a[0] < b[1]:
#             count -= b[1] - a[0]
#     if a[0] <= b[0] <= b[1] <= a[1]:
#         count -= b[1] - b[0]
#     if b[0] <= a[0] <= a[1] <= b[1]:
#         count -= a[1] - a[0]
#     return count
#
# print(hours_overlap([1,4],[5,9]))
res = 0
# for a in times:
#     for b in times:
#         count = 0
#         if a != b:
#             count += hours_overlap(a, b)
#
#     res = max(res, count)
for a in times:
    count = 0
    temps = [z for z in times if z != a]
    for t in range(1001):
        for x in temps:
            if x[0] <= t < x[1]:
                count += 1
                break
    res = max(res, count)
fout.write(str(res)+'\n')


