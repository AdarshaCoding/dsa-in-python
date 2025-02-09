arr = [1, 2, 3, 4, 5, 6]


def sum(arr):
    sum = 0
    for i in range(len(arr)):
        sum = sum + arr[i]
    return sum


# print(sum(arr))
arr = [1, 2, 3, 4, 5, 3, 2, 1]


def remove_duplicates(arr):
    unique_values = set()
    for el in arr:
        unique_values.add(el)
    return list(unique_values)


# print(remove_duplicates(arr))

arr = [4, 3, 5, 1, 3, 5, 6]


def remove_given_number(num):
    pos = -1
    for i in range(len(arr)):
        if arr[i] == num:
            pos = i
            break
    if pos != -1:
        for i in range(pos, len(arr) - 1):
            arr[i] = arr[i + 1]

    return arr[:-1]


# print(remove_given_number(3))

arr1 = [1, 1, 4, 4, 2, 2, 6, 6]
arr2 = [3, 3, 5, 5]


def remove_dup_by_adding(arr1, arr2):
    # print(list(set(arr1 + arr2)))
    unique_arr = []
    seen = set()
    for el in arr1 + arr2:
        # this makes O(1) instead of checking in unique_arr as it takes O(n) overall it becomes O(n**2)
        # now it would O(n) and O(1) => O(n)

        if el not in seen:
            unique_arr.append(el)
            seen.add(el)
    print(unique_arr)


remove_dup_by_adding(arr1, arr2)
