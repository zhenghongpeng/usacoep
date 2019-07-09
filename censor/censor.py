fin = open('censor.in', 'r')
fout = open('censor.out', 'w')
mag = fin.readline().strip()
cen = fin.readline().strip()
while cen in mag:
    mag = mag.replace(cen, '', 1)
fout.write(mag + '\n')
