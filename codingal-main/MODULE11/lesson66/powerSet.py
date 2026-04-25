# Write a Program to find the power set of a set.
# 1) Import the required module:
#    a) Import `math` to calculate powers of 2.
import math
# 2) Create a function to print the power set:
#    a) Take a list (set) and its size as inputs.
#    b) Calculate total subsets using `2^size`.
def printPowerSet(set,setSize):
    powerSetSize=(int)(math.pow(2,setSize))
# 3) Use two loops to generate all subsets:
#    a) Outer loop runs from 0 to (total subsets - 1).
#    b) Inner loop checks each bit position from 0 to (size - 1).
    outer=0
    inner=0
    for outer in range(0,powerSetSize):
        for inner in range(setSize):
            if ((outer & (1 << inner))>0):
                print(set[inner],end="")
        print("")
# 4) Use bitwise AND to decide whether to include an element:
#    a) If `(outer & (1 << inner))` is true, print that element.
#    b) After inner loop, print a new line for the next subset.
          
# 5) Take input from the user:
#    a) Read the number of elements.
#    b) Read each element and store it in a list.
size=int(input("enter the array size"))
set=[]
for i in range(0,size):
    n=int(input("enter the elements"))
    set.append(n)
# 6) Call the function to print the complete power set.
printPowerSet(set,len(set))
