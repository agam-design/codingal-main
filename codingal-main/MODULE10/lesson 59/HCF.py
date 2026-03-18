# Program to find HCF/GCD
# Program to find HCF/GCD
 
# Enter 2 numbers
numberLargest = int(input("Enter Largest number : "))
numberSmallest = int(input("Enter Smallest number : "))
  
# Using Eucliden Algorithms  
while(numberSmallest):
  numberStore = numberSmallest
  numberSmallest = numberLargest % numberSmallest
  numberLargest = numberStore
 
print("HCF is : ",numberLargest)

#let the numbers be 48,18
#48%18=12
#18%12=6
#12%6=0
#here remainder becomes 0. So curent largest value is the GCD/HCF.
#HCF=6





