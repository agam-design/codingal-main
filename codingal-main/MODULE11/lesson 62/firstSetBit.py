# write a program to chcek if the rightmost set bit is a number.
def rightmostSetBitPos(n):
    pos = 1
    while n > 0:
        if n & 1:
            return pos
        n >>= 1
        pos += 1

num = int(input("Enter number: "))
print("Position:", rightmostSetBitPos(num))