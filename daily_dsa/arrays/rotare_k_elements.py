def rotate(arr, k):
    n = len(arr)
    k = k % n  # if "k" is greater than the length of the array
    print(arr[-k:])
    return arr[-k:] + arr[:-k]


arr = [1, 2, 3, 4, 5, 6, 10, 67, 89, 45]
print(rotate(arr, 1))
