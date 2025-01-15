def bubble_sort(arr):
    n = len(arr)
    counter = 0
    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            counter += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break

    return arr, counter


arr = [5, 1, 3, 2, 4]
arr, counter = bubble_sort(arr)

print(arr, counter)
