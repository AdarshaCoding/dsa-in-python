# def sum(x):
#     total_sum = 0  # Op: 1
#     for i in range(x + 1):
#         total_sum = total_sum + x  # Op: loop x time
#     return total_sum


# print(sum(4))


def sum(x):
    total_sum = 0
    for i in range(x + 1):
        total_sum = total_sum + x
    return total_sum


print(sum(4))  # 20
