import string
fin = open('circlecross.in', 'r')
fout = open('circlecross.out', 'w')
circ = fin.readline().strip()
a = ord('A')
d = dict.fromkeys(string.ascii_uppercase, [])
alph = [chr(i) for i in range(a,a+26)]
print(a, d, alph)
for x in alph:
    temp = []
    for y in range(52):
        if circ[y] == x:
            temp.append(y)
    temp2 = []
    for z in range(temp[0]+1, temp[1]):
        temp2.append(circ[z])
        d[x] = temp2
count = 0
for key in d:
    for key2 in d:
        if key != key2:
            if key2 in d[key] and key in d[key2]:
                count += 1
fout.write(str(count//2)+'\n')
