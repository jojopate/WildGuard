def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Get user input
num = int(input("Enter a number: "))

# Calculate factorial
result = factorial(num)

