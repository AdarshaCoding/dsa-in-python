def factorial(n):
    result = 1  # Op: 1
    while n > 1:  # Op: number of iterations
        result = result * n
        n = n - 1
    return result


print(factorial(5))
