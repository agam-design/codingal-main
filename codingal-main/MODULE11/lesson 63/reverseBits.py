# write a program to reverse all bits present in a number and print a newly formed number
def reverseBits(n):
    rev = 0
    while n > 0:
        rev = rev * 2 + (n % 2)
        n = n // 2
    return rev

num = int(input("Enter number: "))
result = reverseBits(num)

print("Reversed bit number:", result)