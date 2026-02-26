def myfunction(n):
    for i in range(0,n+1):
        print("First Loop")
 
    j=1
    while(j<=n+1):
        print("Second Loop ",j)
        j=j*2
 
    for i in range(0,100):
        print("Third loop")

#ANALYSIS
#first loop
#complexity = O(n)

#second loop
#complexity = O(log n)

#third loop
#complexity = O(1) (constant time)

#TOTAL
#O(n) + O(log n) + O(1)= O(n)
#So the time complexity of the above code is:
#O(n)