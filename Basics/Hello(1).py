print("HELLO WORLD")
num = 0

while num != -1:
    num=int(input("Enter a number(-1 to terminate): "))
    square = num * num
    print('Number:', num)
    if (num > 0):
        print(num, "is positive")
        print("Square is: ", square)
    elif (num == -1):
        print("terminating")
    elif (num < 0):
        print(num, "is negative")
        print("Square is: ", square)

    else:
        print(num, "Zero")
print("PROGRAM TERMINATED")
print("Thank you")
