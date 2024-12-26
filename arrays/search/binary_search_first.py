def binary_search_first(arr, target):
    left = 0
    right = len(arr) - 1
    result = -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            result = mid
            right = mid - 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return result


arr = [1, 2, 3, 3, 3, 4, 5]
target = 7
print(binary_search_first(arr, target))
