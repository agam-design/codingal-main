num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Find the greater number
maxNum = max(num1, num2)

while True:
    if maxNum % num1 == 0 and maxNum % num2 == 0:
        lcm = maxNum
        break
    maxNum += 1

print("LCM is:", lcm)