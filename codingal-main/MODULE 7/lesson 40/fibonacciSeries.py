num = int(input("enter a number. "))
a = 0
b = 1
print("fibonacci: ")

for i in range(num):
    print(a, end=" ")
    nextNumber = a + b
    a = b
    b = nextNumber