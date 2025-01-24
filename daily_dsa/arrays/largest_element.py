# Brute Force Solution
def largest_brute_force(arr):
    arr.sort()
    n = len(arr)
    print(arr[n - 1])


# Optimal Solution
def largest_element(arr):
    largest = arr[0]
    for i in range(len(arr)):
        if arr[i] > largest:
            largest = arr[i]
    return largest


arr = [1, 2, 4, 15, 16, 18, 19, 11, 12]
print(largest_element(arr))
largest_brute_force(arr)
