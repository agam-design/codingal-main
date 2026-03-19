# Program to check if the user entered number is odd or even using only bitwise operator
# Returns true if n is even, else odd

#for binary numbers, if last bit=0 then the number would be even.example 100=4, even number.
#if last bit=1 , then the number would be odd.example 101=5, odd number.

def isEvenOdd( n) :
    # XOR with 1 equals n+1
    if (n ^ 1 == n + 1) :
        return True
    else :
        return False
 
number = int(input("Enter your number : "))
 
if isEvenOdd(number):
    print(number," is Even")
else:
    print(number," is Odd")



