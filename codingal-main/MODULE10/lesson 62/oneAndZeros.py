# Write a Program to find the number of zero bits and one bit present in a number.
def numOfBits (n):
    zeros=0
    ones=0
    while (n):
        if (n&1==1):
            ones+=1
        else:
            zeros+=1
            
        n>>=1#right shift the number to remove the last bit that we just checked above.
    print("ones= ", ones, "zeros= ", zeros)
    
num=int(input("enter your number."))
numOfBits(num)
#SET BIT= a bit that is 1.
