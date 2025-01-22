def two_sum(arr, target):
    values_set = {}

    for i, value in enumerate(arr):
        diff = target - value
        if diff in values_set:
            return [values_set[diff], i]
        values_set[value] = i


arr = [2, 5, 9, 4, 6, 10]
target = 10
print(two_sum(arr, target))
