# Write a Program to find the element not making a pair.
#program to find element that appears an odd number of times in an array.
# Program to find the element not making a pair
# Function to calculate the number that is odd occurring 
 
def OddOccurring(arr):
 
    # Initialize result
    res = 0
     
    # Traverse the array
    for element in arr:
        # XOR with the result
        res = res ^ element
 
    return res
 
# Initialize our array
arr = []
 
# Take array size as input
n = int(input("Enter array size : "))
 
# Take array element input 
while(n):
    num = int(input("Enter number : "))
    arr.append(num)
    n-=1
 
print("\n\nOdd occurring number is : ",OddOccurring(arr))
# Example:
# [2, 3, 2, 4, 4]
# Step-by-step:
# res = 0
# res = 0 ^ 2 = 2
# res = 2 ^ 3 = 1
# res = 1 ^ 2 = 3
# res = 3 ^ 4 = 7
# res = 7 ^ 4 = 3
# Final result = 3 (the odd occurring number)

#the time complexity is  O(n).




