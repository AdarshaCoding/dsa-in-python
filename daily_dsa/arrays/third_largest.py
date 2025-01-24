def third_largest(arr):
    largest = arr[0]
    slargest = float("-inf")
    tlargest = float("-inf")

    for i in range(len(arr)):
        if arr[i] > largest:
            tlargest = slargest
            slargest = largest
            largest = arr[i]
        elif arr[i] > slargest and arr[i] != largest:
            tlargest = slargest
            slargest = arr[i]
        elif arr[i] > tlargest and arr[i] != largest and arr[i] != slargest:
            tlargest = arr[i]

    return tlargest


arr = [1, 2, 3, 10, 15, 20, 34, 25]
print(third_largest(arr))
