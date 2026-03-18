# Program to check if the given number is a palindrome
num=int(input("enter a number: "))
orginalNum=num
reversedNum= 0

while num>0:
    digit=num%10 #% is the modulus operator.On dividing it will give the remainder
    reversedNum=reversedNum*10+digit
    num//=10 #// is the floor division operator.It will give the quotient after removing the decimal part.

if orginalNum== reversedNum:
    print(orginalNum ,"is a palindrome")
else:
    print(orginalNum ,"is not a palindrome")