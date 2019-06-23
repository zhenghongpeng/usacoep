fin = open('censor.in', 'r')
fout = open('censor.out', 'w')
mag = fin.readline().strip()
cen = fin.readline().strip()
while True:
    if cen in mag:
        mag = mag.replace(cen, '', 1)
    else:
        break
def helper(cen, mag):
    if cen in mag:
        return helper(mag.replace(cen,'',1))
    else:
        return mag
def helper2(mag):

    return helper2(mag.replace(cen,'',1))

fout.write(helper2(mag) + '\n')
