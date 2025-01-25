# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     return n * factorial(n - 1)


def factorial(n):
    memo = {0: 0, 1: 1}

    def f(n):
        if n in memo:
            return memo[n]

        memo[n] = f(n - 1) + f(n - 2)
        return memo[n]

    return f(n)


print(factorial(4))
