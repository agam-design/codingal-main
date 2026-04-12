# Write a program to divide two numbers without using the division operator.
def divide(dividend, divisor):
    sign=(-1 if((dividend<0)^(divisor<0))else 1)
    ourDividend=abs(dividend)
    ourDivisor=abs(divisor)
    quotientNum=0
    tempNum=0
    
    for i in range(31,-1,-1):
        if(tempNum+(ourDivisor<<i)<=ourDividend):
            tempNum+=ourDivisor<<i
            quotientNum|=1<<i
        if sign==-1:
            quotientNum=-quotientNum
    return quotientNum
a=int(input("enter a value for a in a/b: "))
b=int(input("enter a value for b in a/b: "))
print("result= ", divide(a,b))
#time complexity= constant , O(1)

