# def problem_1():
#     arr = [1, 2, 3, 4, 5]

#     sum = 0  # Op: 1 : O(1)
#     for el in arr:
#         sum = sum + el  # Op: number of iterations : n times : O(n)
#     print(sum)  # 15

#     product = 1  # Op: 1 : O(1)
#     for el in arr:
#         product = product * el  # Op: number of iterations : n times : O(n)
#     print(product)  # 120


# problem_1()
# # Time Comlexity:  1 + n + 1 + n =>  2+ 2n =>  2n =>  n => O(n)


# def problem_2():
#     arr = [1, 2, 3, 4, 5]
#     counter = 0
#     for i in arr:
#         for j in arr:
#             counter += 1
#             print(i, j)
#     print(
#         f"Total Iteration count (n**2): {counter} and length of the array: {len(arr)}"
#     )  # n2 => 5**2 = 25


# problem_2()


# # Liner search : O(n)
# def problem_2():
#     arr = [1, 2, 3, 4, 5]
#     target = 4
#     for el in arr:
#         if el == target:  # number of iterations
#             return True
#     return False


# print(problem_2())


# def intTostr(n):
#     digits = "0123456789"
#     result = ""
#     if n == 0:
#         return "0"
#     while n > 0:
#         result = result + digits[n % 10]
#         n = n // 10
#     return result


# print(intTostr(123))
# print(type(intTostr(123)))


# def reverse(n):
#     digits = "0123456789"
#     if n == 0:
#         return 0
#     result = ""
#     while n > 0:
#         result = result + digits[n % 10]
#         n = n // 10
#     return result


# print(reverse(123))
# print(type(reverse(123)))


# def revereStr(s):
#     if s == "":
#         return None
#     result = ""
#     for i in s:
#         result = i + result
#     return result


# print(revereStr("abcd"))
# print("abcdef"[::-1])


# def problem_3():
#     n = 100
#     for i in range(n // 2, n + 1):  # Outer loop: from n/2 to n
#         counter = 0
#         j = 2  # Start j at 2
#         while j <= n:  # Inner loop: while j is <= n
#             counter += 1
#             print(counter, end=" ")
#             j = j * 2  # Double the value of j in each iteration
#         print()  # Print a new line after each outer loop iteration


# problem_3()


# def reverse_list():
#     arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#     n = len(arr) // 2
#     counter = 0
#     for i in range(0, n):
#         other = len(arr) - i - 1
#         counter += 1
#         temp = arr[i]
#         arr[i] = arr[other]
#         arr[other] = temp
#     print(arr)
#     print(counter)


# reverse_list()


def sum_of_digits(n):
    sum = 0
    while n > 0:
        sum = sum + (n % 10)
        n = n // 10
    print(sum)


sum_of_digits(1235)
