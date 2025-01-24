def second_largest(arr):
    largest = arr[0]
    slargest = float("-inf")
    for i in range(len(arr)):
        if arr[i] > largest:
            slargest = largest
            largest = arr[i]
        elif arr[i] > slargest and arr[i] != largest:
            slargest = arr[i]
    return slargest


arr = [1, 2, 7, 7, 5]
print(second_largest(arr))
