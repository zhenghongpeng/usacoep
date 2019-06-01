fin = open('cbarn.in', 'r')
fout = open('cbarn.out', 'w')
n = int(fin.readline().strip())
nums = []
for x in range(n):
    nums.append(int(fin.readline().strip()))
answer = -1
for x in nums:
    result = 0
    result2 = 0
    for y in nums:
        if nums.index(y)-nums.index(x) > 0:
            result += y * abs(nums.index(y)-nums.index(x))
        if nums.index(y)-nums.index(x) <= 0:
            result += y * (n-abs(nums.index(y) - nums.index(x)))
        if nums.index(y) - nums.index(x) <= 0:
            result2 += y * abs(nums.index(y) - nums.index(x))
        if nums.index(y) - nums.index(x) > 0:
            result2 += y * (n - abs(nums.index(y) - nums.index(x)))
    result = min(result, result2)
    if answer == -1:
        answer = result
    if answer != -1:
        if answer == 46:
            print(x)
        answer = min(answer, result)
fout.write(str(answer) + '\n')
