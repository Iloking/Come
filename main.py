# Sum of n numbers for a given input

# Algorithm - 1
def func1(n):
    iteration = 0
    iteration += 1
    print("For Algo 1:", n, "Iteration:", iteration)
    return n * (n + 1) / 2

print(func1(5))


# Algorithm - 2
def func2(n):
    iteration = 0
    sum = 0
    for i in range(1, n+1):
        sum = sum + i
        iteration += 1
    print("For Algo 2:", n, "Iteration:", iteration)
    return sum

print(func2(5))

# Algorithm - 3
def func3(n):
    sum = 0
    iteration = 0
    for i in range(1, n+1):
        for j in range(1, i+1):
            sum = sum + 1
            iteration += 1
    print("For Algo 3:", n, "Iteration:", iteration)
    return sum

print(func3(5))
