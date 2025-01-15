# arr = [1, 2, 3, 4, 5]
# print("index and values")
# for i in range(len(arr)):
#     print(i, arr[i])

# print("array elements")
# for el in arr:
#     print(el, end=" ")
# print("enumerate - counter")
# for i, el in enumerate(arr, start=10):
#     print(i, el)

# print("List comprehension")
# # new_list = [expression for item in iterable if condition]
# squared_arr = [x**2 for x in arr]
# print(squared_arr)
# squared_arr = [x**2 for x in arr if x >= 3]
# print(squared_arr)
# pairs = [(x, y) for x in arr for y in arr]
# print(pairs)

# nested_arr = [[1, 2, 3, 4], [[5], [10, 20], [6]], [7, 8]]  # all array should be nested
# flatten_arr = [item for sub_array in nested_arr for item in sub_array]
# print(flatten_arr)

# # nested_arr_1 = [1, 2, 3, [4, [10, 20, [50, 80], 30], 5]]
# nested_arr_1 = [1, 2, 3, [4, [10, [77, 66, 88], 30], 5]]
# flat_array = []


# def flatten_array(arr):
#     for el in arr:
#         if isinstance(el, list):
#             flatten_array(el)
#         else:
#             flat_array.append(el)
#     return flat_array


# # print(flatten_array(nested_arr_1))


# def flatten_array_depth(arr, depth):
#     for el in arr:
#         if isinstance(el, list) and depth > 0:
#             depth = depth - 1
#             flatten_array_depth(el, depth)

#         else:
#             flat_array.append(el)
#     return flat_array


# print(flatten_array_depth(nested_arr_1, 2))


arr = [5, 1, 3, 2, 4]


def bubble_sort(arr):
    print(arr)
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp

    print(arr)


# bubble_sort(arr)


def selection_sort(arr):
    print(arr)

    for i in range(len(arr)):
        min_idx = i

        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]


selection_sort(arr)
