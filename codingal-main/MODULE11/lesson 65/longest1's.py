n = int(input("Enter a number: "))

binary = bin(n)[2:]   
count = 0
maxCount = 0

for bit in binary:
    if bit == '1':
        count += 1
        if count > maxCount:
            maxCount = count
    else:
        count = 0

print("Binary:", binary)
print("Longest consecutive 1's:", maxCount)