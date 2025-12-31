num = int(input("enter the number to check "))
flag = False
if num>1:
    for i in range(2,num):
        if (num%i)==0:
            flag=  True
            break
if flag:#when flag is true
    print(num,"is not a prime number")
else:
    print(num, "is a prime number")