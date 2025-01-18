# Pattern: Sliding Window
def max_sum_subarray(arr, k):
    n = len(arr)
    window_sum = sum(arr[:k])
    max_sum = window_sum

    for i in range(k, n):
        window_sum = window_sum + arr[i] - arr[i - k]
        max_sum = max(max_sum, window_sum)

    return max_sum


print(max_sum_subarray([1, 2, 3, 4, 5, 6], 3))
