num = int(input("enter a number. "))

def factorial(n):
    if n ==1:
        return n
    else:
        return n*factorial(n-1)
    
if num<0:
    print("factorial does not exist. ")
elif num==0:
    print("factorial of 0 is 1 ")
else:
    print("factorial of " ,num," is ",factorial(num))