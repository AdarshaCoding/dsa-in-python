arr = [2, 7, 1, 5, 20, 16, 11, 15]
target = 25


def two_sum_problem(arr, target):
    hashmap = {}
    for i, el in enumerate(arr):
        diff = target - el
        if diff in hashmap:
            return [hashmap[diff], i]
        hashmap[el] = i
    return []


result = two_sum_problem(arr, target)
print(result)
