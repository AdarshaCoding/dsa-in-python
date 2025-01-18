def find_large_small_element(arr):
    arr.sort()
    print("Smallest", arr[0])
    print("Largest", arr[-1])


arr = [4, 10, 76, 59, 40, 88]
find_large_small_element(arr)
