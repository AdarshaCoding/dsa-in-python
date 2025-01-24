def check_isSorted(arr):
    for i in range(len(arr) - 1):
        if arr[i] < arr[i + 1]:
            pass
        else:
            return False
    return True


arr = [1, 2, 10, 3, 4, 5]
print(check_isSorted(arr))
