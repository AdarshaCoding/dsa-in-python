lst = [0, 1, 2, 0, 3, 0, 4]


def move_zeros_to_end(lst):
    non_zeros = [x for x in lst if x != 0]
    zeros = [0] * (len(lst) - len(non_zeros))
    return non_zeros + zeros


result = move_zeros_to_end(lst)
print(result)

# min and max
lst = [5, 49, 6, 8, 3, 15]
print(min(lst), max(lst))

# reverse
lst.reverse()
print(lst)
print(lst[::-1])

# remove duplicates
lst = [4, 5, 9, 4, 6, 7, 2, 4, 5, 10, 15, 3, 6, 10, 15]
print(list(set(lst)))

# Intersection of two list or common elements b/w two lists - "&" symbol is used

lst_1 = [4, 7, 5, 8, 1, 2]
lst_2 = [8, 4, 9, 10]
print(list(set(lst_1) & set(lst_2)))

lst_3 = [4, 88, 7, 1, 3, 9, 10, 66, 33, 44]
# Max element index
print(lst_3.index(max(lst_3)))
