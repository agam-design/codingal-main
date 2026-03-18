# Take a number input from the user and check if it is prime
from math import sqrt
num =int(input("enter a number: "))
if num>1:
    for i in range(2,int(sqrt(num)+1)):
        if (num % i)== 0:# % is the modulus operator, it will check with the remainder. Here its checking whether the number divided by i gives remainder 0.That is checking if it is divisible by i or not.
            print("it is not a prime number.")
            break
    else:
        print("it is a prime number.")
else:
    print("it is not a prime number.") 