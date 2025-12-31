# *
# **
# ***
# ****
n = int(input("enter the number of rows "))
for i in range(0,n):
    for j in range(0,i+1):
         print("*", end=" ") #end=" " will tell python to not go to next line., just print a space after star.

    print("\n")