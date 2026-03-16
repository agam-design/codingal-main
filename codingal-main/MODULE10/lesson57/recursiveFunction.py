def myfunction1(n):
    if(n>0):
        return
    for i in range (0,n+1):
        print("Codingal")
    myfunction1(n/2)
    myfunction1(n/3)

# recurrence relation will 
# T(n) = T(n/2) + T(n/3) + O(n)

def myfunction2(n):
    if(n<=1):
        return
    print("Codingal")
    myfunction2(n-1)
    
# recurrence relation will be
# T(n) = T(n-1) + O(1)
