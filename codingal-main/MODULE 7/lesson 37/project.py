x = input("enter the value of x ")
y = input("enter the value of y ")
z = input("enter the value of z ")
temp = x
x = y
y = temp
y = z
z = temp
z = x
print("the value of x after swapping is ", x)
print("print the value of y after swapping is ", y)
print("print the value of z after swapping is ", z)