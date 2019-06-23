cubes = [1,8,27,64]
for A in range(1,10):
    for B in range(10):
        for C in range(10):
            if 100*A+10*B+C-100*B-10*C-A in cubes and B != 0 and A != B and A != C and B != C:
                print(100*A+10*B+C, 100*B+10*C+A)
            if 100*A+10*B+C-100*C-10*A-B in cubes and C != 0 and A != B and A != C and B != C:
                print(100*A+10*B+C, 100*C+10*A+B)