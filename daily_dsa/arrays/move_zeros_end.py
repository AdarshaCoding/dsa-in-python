def move_zeros_to_end(arr):
    n = len(arr)
    zeros_count = 0
    new_arr = []
    for el in arr:
        if el == 0:
            zeros_count += 1
        else:
            new_arr.append(el)
    for _ in range(zeros_count):
        new_arr.append(0)

    print(new_arr)


arr = [0, 1, 0, 2, 0, 0, 4, 5, 0]
move_zeros_to_end(arr)
