# Write a Program to swap two numbers without using a third variable.
#swapping 2 numbers using bytewise XOR operator.
def swap (a,b):
    a=a^b
    b=a^b 
    a=a^b
    print("after swapping a=", a ,"b= ", b)
swap(24,12)
#time complexity= 3 XOR operations are used and each is of constant time.
#so time complexity= O(1) 
#space complexity=O(1) 