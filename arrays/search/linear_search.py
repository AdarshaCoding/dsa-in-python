arr = [10, 40, 22, 13, 53, 67, 70]


def linear_search(arr, key):
    for el in arr:
        if el == key:
            return True
    return False


key = int(input("Enter the value to search: "))
print(linear_search(arr, key))
