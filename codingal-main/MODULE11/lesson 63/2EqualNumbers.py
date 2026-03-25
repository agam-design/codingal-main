# Write a Program to check if two numbers are equal without using any comparison operator.
num1= int(input("enter first number"))
num2= int(input("enter the second number"))
def ifSame(num1, num2):
    if ((num1^num2)!=0):# bitwise xor operator is used.
        print("the numbers are not equal.")
    else:
        print("the numbers are equal.") 
ifSame(num1, num2)  
#when we do xor 2 numbers 
#if they are same the result is 0.
#if the are different the result is non zero.