# Pattern: Two pointer approach
def two_sum(arr, target):
    left = 0
    right = len(arr) - 1
    while left < right:
        sum = arr[left] + arr[right]
        if sum == target:
            return [left, right]
        elif sum < target:
            left += 1
        else:
            right -= 1
    return "No Match Found!"


arr = [2, 3, 4, 5, 8, 10]
print(two_sum(arr, 9))
