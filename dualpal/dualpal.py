"""
ID: ericvpe4
LANG: PYTHON3
TASK: dualpal
"""
import time
start = time.time()
fin = open ('dualpal.in', 'r')
fout = open ('dualpal.out', 'w')
def baseN(num,n):
    new_num_string=''
    current=num
    while current!=0:
        remainder=current%n
        remainder_string=str(remainder)
        new_num_string=remainder_string+new_num_string
        current=current//n
    return new_num_string
def baseN2(num,b,numerals="0123456789abcdefghijklmnopqrstuvwxyz"):
    return ((num == 0) and numerals[0]) or (baseN2(num // b, b, numerals).lstrip(numerals[0]) + numerals[num % b])
N,S = map(int, fin.readline().split())
counting = 0
curnum = S+1
def ifpal(number):
    return number == number[::-1]
while counting < N:
    bcount = 0
    for b in range(2,11):
        if ifpal(baseN(curnum,b)):
            bcount +=1

        if bcount ==2:
            counting += 1
            fout.write(str(curnum) + "\n")
            break
    curnum += 1

end = time.time()
print (end-start)


