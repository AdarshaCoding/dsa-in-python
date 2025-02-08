def search_for_element(arr, target):
    for el in arr:
        if el == target:
            return True
    return False


arr = [1, 2, 3, 4, 5]
target = 5
print(search_for_element(arr, target))
# O(n) - searchin for last element
# o(1) - if element found at first position
