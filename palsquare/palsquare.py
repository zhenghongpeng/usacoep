"""
ID: ericvpe4
LANG: PYTHON3
TASK: palsquare
"""


fin = open ('palsquare.in', 'r')
fout = open ('palsquare.out', 'w')

base = int(fin.readline().strip())

def ifpal(number):
    return number == number[::-1]
def baseN(num,n):
    num_rep={10:'a',
         11:'b',
         12:'c',
         13:'d',
         14:'e',
         15:'f',
         16:'g',
         17:'h',
         18:'i',
         19:'j',
         20:'k',
         21:'l',
         22:'m',
         23:'n',
         24:'o',
         25:'p',
         26:'q',
         27:'r',
         28:'s',
         29:'t',
         30:'u',
         31:'v',
         32:'w',
         33:'x',
         34:'y',
         35:'z'}
    new_num_string=''
    current=num
    while current!=0:
        remainder=current%n
        if 36>remainder>9:
            remainder_string=num_rep[remainder]
        elif remainder>=36:
            remainder_string='('+str(remainder)+')'
        else:
            remainder_string=str(remainder)
        new_num_string=remainder_string+new_num_string
        current=current//n
    return new_num_string
for i in range(1, 301):
    if ifpal(baseN(i**2,base)):
        fout.write((str(baseN(i,base)) + ' ' + baseN(i**2,base) + '\n').upper())


