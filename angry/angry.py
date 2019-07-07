import sys
fin = open('angry.in', 'r')
fout = open('angry.out', 'w')
def getExplosionIndex(location, startIndex, goLeft):
    lastExplosionIndex = startIndex
    currentRadius = 1
    while lastExplosionIndex > 0 and lastExplosionIndex < len(location) - 1:
        if goLeft:
            direction = -1
        else:
            direction = 1
        nextIndex = lastExplosionIndex
        while (nextIndex + direction >= 0 and nextIndex + direction < len(location) and abs(location[nextIndex + direction] - location[lastExplosionIndex]) <= currentRadius):
            nextIndex += direction
        if nextIndex == lastExplosionIndex:
            break
        lastExplosionIndex = nextIndex
        currentRadius += 1
    return lastExplosionIndex
N = int(fin.readline().strip())
loc = []
for x in range(N):
    loc.append(int(fin.readline().strip()))
locations = sorted(loc)
answer = 1
for start in range(N):
    leftMostExplosion = getExplosionIndex(locations, start, True)
    rightMostExplosion = getExplosionIndex(locations, start, False)
    numExploded = rightMostExplosion - leftMostExplosion + 1
    if numExploded > answer:
        answer = numExploded
fout.write(str(answer)+'\n')
