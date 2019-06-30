fin = open ('traffic.in', 'r')
fout = open ('traffic.out', 'w')
# N = int(fin.readline().strip())
# logs = []
# for x in range(N):
#     logs.append(fin.readline().split())
#     logs[x][1], logs[x][2] = int(logs[x][1]), int(logs[x][2])
# min1 = 0
# max1 = 0
# min2 = 0
# max2 = 0
#
#
# def consecutive_nones():
#     for x in logs:
#         if logs.index(x) != len(logs)-1:
#             if x[0] == 'none' and logs[logs.index(x)+1][0] == 'none':
#                 return True
#     return False
#
#
# def combine_consecutive_nones():
#     for x in logs:
#         if logs.index(x) != len(logs)-1:
#             if x[0] == 'none' and logs[logs.index(x)+1][0] == 'none':
#                 logs[logs.index(x) + 1] = ['none', max(x[1], logs[logs.index(x) + 1][1]), min(x[2], logs[logs.index(x)+1][2])]
#                 logs.pop(logs.index(x))
#                 break
#
#
# while consecutive_nones():
#     combine_consecutive_nones()
# for x in range(len(logs)):
#     if logs[x][0] == 'on':
#         min1 -= logs[x][2]
#         max1 -= logs[x][1]
#     elif logs[x][0] == 'off':
#         min1 += logs[x][1]
#         max1 += logs[x][2]
#     else:
#         min1 += logs[x][1]
#         max1 += logs[x][2] #x
#         break
# for x in range(len(logs)):
#     if logs[len(logs)-1-x][0] == 'on':
#         min2 += logs[len(logs)-1-x][1]
#         max2 += logs[len(logs)-1-x][2]
#     elif logs[len(logs)-1-x][0] == 'off':
#         min2 -= logs[len(logs)-1-x][2]
#         max2 -= logs[len(logs)-1-x][1]
#     else:
#         min2 += logs[len(logs)-1-x][1]
#         max2 += logs[len(logs)-1-x][2] #x
#         break
# fout.write(str(max(0, min1))+' '+str(max1)+'\n'+str(max(0, min2))+' '+str(max2))
#
A = []
B = []
T = []
N = int(fin.readline().strip())
for x in range(N):
    mrgle = fin.readline().split()
    T.append(mrgle[0])
    A.append(int(mrgle[1]))
    B.append(int(mrgle[2]))
a = -999999999
b = 999999999
for x in range(N):
    if T[N-1-x] == 'none':
        a = max(a, A[N-1-x])
        b = min(b, B[N-1-x])
    if T[N-1-x] == 'off':
        a += A[N-1-x]
        b += B[N-1-x]
    if T[N-1-x] == 'on':
        a -= B[N-1-x]
        b -= A[N-1-x]
        a = max(0, a)
fout.write(str(a)+' '+str(b)+'\n')
a = -999999999
b = 999999999
for x in range(N):
    if T[x] == 'none':
        a = max(a, A[x])
        b = min(b, B[x])
    if T[x] == 'on':
        a += A[x]
        b += B[x]
    if T[x] == 'off':
        a -= B[x]
        b -= A[x]
        a = max(0, a)
fout.write(str(a)+' '+str(b)+'\n')