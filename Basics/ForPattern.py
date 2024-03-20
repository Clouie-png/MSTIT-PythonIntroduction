def printPattern(rMax, cMax):
    for r in range(rMax):
        print('')
        for c in range(cMax):
            if r == 0 or c == 9 or c == 0 or r == 9 or r == c:
                print("0\t", end='')
            else:
                print("-\t", end='')
n1 = 10
n2 = 10
printPattern(n1,n2)