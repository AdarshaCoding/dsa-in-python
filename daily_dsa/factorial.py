# Day_2 - 16/01/2025
# Factorial of a given number


def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)


result = factorial(4)  # 4! = 4 * 3 * 2 * 1
print(result)

print(factorial(5))
