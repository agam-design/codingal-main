num = int(input("enter a number "))

digits = str(num)
power = len(digits)
total = 0

for d in digits:
    total+= int(d) ** power

if total == num:
    print("Armstrong Number")
else:
    print("Not an Armstrong number")
