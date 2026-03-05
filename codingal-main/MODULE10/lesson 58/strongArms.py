num = int(input("Enter a number: "))
Digits = len(str(num))

sum= 0
temp = num

while temp > 0:
    digit= temp % 10 # %10 (remainder) gives the last digit. % is the modulus operator.
    sum += digit ** Digits
    temp //= 10# //10 (floor division) removes the last digit.
    
if num == sum:
    print("It's an armstrong number")
else:
    print("It's not an armstrong number")


# num = int(input("Enter a number: "))


# numDigits = len(str(num))

# sum= 0
# temp = num

# while temp > 0:
#     digit= temp % 10 # %10 (remainder) gives the last digit. % is the modulus operator.
#     sum += digit ** 3 
#     temp //= 10# //10 (floor division) removes the last digit.
    
# if num == sum:
#     print("It's an armstrong number")
# else:
#     print("It's not an armstrong number")

