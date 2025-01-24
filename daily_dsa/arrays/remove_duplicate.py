# def remove_duplicate(arr):
#     unique_set = set()
#     for el in arr:
#         unique_set.add(el)
#     return len(unique_set)


def remove_duplicate(arr):
    i = 0
    for j in range(1, len(arr)):
        if arr[i] != arr[j]:
            arr[i + 1] = arr[j]
            i += 1
    return i + 1


arr = [1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4]
print(remove_duplicate(arr))
