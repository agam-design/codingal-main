n = int(input("Enter a number: "))

if n <= 0:
    print("Not a power of 8")
else:
    while n % 8 == 0:
        n = n // 8

    if n == 1:
        print("Power of 8")
    else:
        print("Not a power of 8")