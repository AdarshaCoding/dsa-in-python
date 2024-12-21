arr = [1, 2, 3, 4, 5, 6, 7]


def binary_search(arr, key):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == key:
            return True
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return False


key = int(input("Enter the value to search: "))
print(binary_search(arr, key))
