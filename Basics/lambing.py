sum = 0
limit = int(input("Enter a num: "))
fact2 = 1
for ctr in range(1,limit + 1):
    print(ctr)
    sum = sum + ctr
    fact2 = fact2 * ctr
print()
print(sum)
print(fact2)
