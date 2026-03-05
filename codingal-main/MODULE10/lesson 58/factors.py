num = int(input("Enter a Number: "))
def printFactors (x):
    print("factors are: ")
    for i in range(1, x+1):
        if x % i==0: #% is the modulus operator.this will check the remainder.
            print(i)
printFactors(num)
    