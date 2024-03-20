def printPattern():
    for r in range(14):
        print('')
        for c in range(6):
            if r % 2 :
                print("1\t", end='')
            else:
                print("0\t", end='')

printPattern()