# Write a Program to check if the Nth bit is set or not.
def setOrNot(num,n):
    if num&(1<<(n-1)):
        print("set")
    else:
        print("not set")
num=int(input("enter the number."))
n=int(input("enter a bit position"))
setOrNot(num,n)
