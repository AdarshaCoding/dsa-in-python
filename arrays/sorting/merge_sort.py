# Merge Sort Algorithm in Python


def merge_sort(arr):
    # Base case: if the list has only one element, return it
    if len(arr) <= 1:
        return arr

    # Split the list into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Recursively split and merge the two halves
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)

    # Merge the sorted halves
    return merge(left_sorted, right_sorted)


def merge(left, right):
    # Merging two sorted lists
    sorted_list = []
    i = j = 0

    # Compare elements of both lists and append the smaller one to the sorted list
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1

    # Append remaining elements from left or right if any
    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])

    return sorted_list


# Example usage
arr = [5, 1, 3, 2, 4]
sorted_arr = merge_sort(arr)
print("Sorted array:", sorted_arr)
