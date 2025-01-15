def selection_sort(arr):
    print(arr)
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    print(arr)


arr = [5, 1, 3, 2, 4]
selection_sort(arr)
