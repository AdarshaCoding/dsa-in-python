# Daily_17/01/2025
def binary_search(arr, key):
    left = 0
    right = len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] == key:
            return True
        elif arr[mid] < key:
            left = mid + 1
        else:
            right = mid - 1
    return False


arr = [2, 6, 8, 10, 50, 56]
print(binary_search(arr, 76))
