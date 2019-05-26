"""
ID: ericvpe4
LANG: PYTHON3
TASK: friday
"""
fin = open ('friday.in', 'r')
fout = open ('friday.out', 'w')
years = int(fin.readline().strip())
def ifleap(y):
    if y % 4 == 0:
        if y % 100 != 0:
            return True
        if y % 400 == 0:
            return True
    return False
freqcounts = {
    0:0,
    1:0,
    2:0,
    3:0,
    4:0,
    5:0,
    6:0
}
months = [31, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30]
#December first
def thirteenth(years):
    day = 3
    for i in range(1900, 1900+years):
        for month in months:
            if ifleap(i) and month == 28:
                day = (day + month + 1) % 7
                freqcounts[day] += 1
            else:
                day = (day + month) % 7
                freqcounts[day] += 1
thirteenth(years)
fout.write(str(freqcounts[6]) + " " + str(freqcounts[0]) + " " + str(freqcounts[1]) + " " + str(freqcounts[2]) + " " + str(freqcounts[3]) + " " + str(freqcounts[4]) + " " + str(freqcounts[5]) + "\n")



