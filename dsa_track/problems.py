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
