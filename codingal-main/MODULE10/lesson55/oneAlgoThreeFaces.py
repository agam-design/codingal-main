def fun1(n):#formula method, directly uses a mathematical formula
    return n*(n+1)/2
print(fun1(4))

#loop method
def fun2(n):
    sum=0
    for i in range(1,n+1):
        sum+=i
        
#nested loop method
def fun3(n):
    sum=0
    for i in range(1,n+1):
        for j in range(i,i+1):
            sum+=1
    return sum

#summary
# here best and fastest method is the formula method
# fun2-medium(loop method)
# fun3-slowest(nested loop)
