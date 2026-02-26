def iteration(n, m):
    result = 0
    for i in range(m):
        result += n
    return result

def recursion(n, m):
    if m == 0:
        return 0
    return n + recursion(n, m - 1)

n = 5
m = 3

print("Iteration RESULT:", iteration(n, m))
print("Recursion RESULT:", recursion(n, m))

#ANALYSIS
#iteration
#speed is faster
#takes less space

#recursion
#speed is slow
#take more space