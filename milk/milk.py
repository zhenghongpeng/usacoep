"""
ID: ericvpe4
LANG: PYTHON3
TASK: milk
"""
fin = open('milk.in', 'r')
fout = open('milk.out', 'w')
cost = 0
Needed, Farmers = map(int, fin.readline().split())
PriceAndAmount = []
for i in range(Farmers):
    Price, Amount = map(int, fin.readline().split())
    PriceAndAmount.append([Price, Amount])
PriceAndAmount = sorted(PriceAndAmount)
for i in range(Farmers):
    if PriceAndAmount[i][1] <= Needed:
        Needed = Needed - PriceAndAmount[i][1]
        cost += PriceAndAmount[i][0] * PriceAndAmount[i][1]
    else:
        cost += Needed * PriceAndAmount[i][0]
        break
fout.write(str(cost) + "\n")
