def search_insertion_position(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left


arr = [1, 3, 6, 7, 9]
target = 8
print(search_insertion_position(arr, target))
