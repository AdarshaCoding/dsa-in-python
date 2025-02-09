def triangle(n):
    for i in range(n):
        for _ in range(i + 1):
            print("*", end=" ")
        print()


# triangle(5)


def triangle(n):
    for i in range(n):
        for _ in range(i, n):
            print("*", end=" ")
        print()


# triangle(5)


def triangle(n):
    for i in range(1, n + 1):
        print(" " * (n - i) + "*" * i)

    for i in range(1, n + 1):
        print(" * " * i)

    for i in range(1, n + 1):
        print(" " * (n - i) + "*" * (2 * i - 1))


triangle(4)

#    *
#   * *
#  * * *
# * * * *
