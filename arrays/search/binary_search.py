arr = [1, 2, 3, 4, 5, 6, 7]


def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return False


target = int(input("Enter the value to search: "))
print(binary_search(arr, target))
