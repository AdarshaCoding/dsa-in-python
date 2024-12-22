arr = [1, 3, 4, 2, 2]


# O(n^2)
def brute_force_duplicate_search(arr):
    for i in range(len(arr) - 1):  # O(n) - no need to check the last element
        for j in range(i + 1, len(arr)):  # O(n)
            if arr[i] == arr[j]:
                return True
    return False


print(brute_force_duplicate_search(arr))


# O(nlogn)
def better_duplicate_search(arr):
    arr.sort()  # O(nlogn)
    for i in range(len(arr) - 1):  # O(n)
        if arr[i] == arr[i + 1]:
            return True
    return False


print(better_duplicate_search(arr))


# O(n) - using dictionary
def smart_duplicate_search(arr):
    dictionary = dict()
    if len(arr) < 2:
        return False
    for i in range(len(arr)):
        if arr[i] in dictionary:
            return True
        else:
            dictionary[arr[i]] = True
    return False


print(smart_duplicate_search([1, 2, 4, 5, 4]))
