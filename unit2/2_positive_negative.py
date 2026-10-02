num = float(input("Enter number: "))

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

if num > 0:
    if num == int(num):
        if int(num) % 2 == 0:
            print("Even integer")
        else:
            print("Odd integer")
    else:
        print("Decimal")