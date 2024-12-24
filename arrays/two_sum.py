arr = [2, 7, 11, 15]
target = 17


def two_sum_problem(arr, target):
    hash_map = {}
    for i, el in enumerate(arr):
        difference = target - el
        if difference in hash_map:
            return [hash_map[difference], i]

        hash_map[el] = i
    return []


result = two_sum_problem(arr, target)
print(result)
