# Write a Python program to check whether a number entered by the user is greater than 50 or not. Also, if it is greater than 50, then check whether it is odd or even.
num = int(input("enter the number. "))
if num>50:
    print("number is greater than 50. ")
    if num%2==0:
        print("the number is even. ")
    else:
        print("the number is odd. ")
    
else:
    print("the number is less than 50. ")