from sys import getsizeof

arr = []
for i in range(100):
    print(i, getsizeof(arr))
    arr.append(i)

# Initally, 1 block
# increased 4 more blocks
# increased 4 more blocks then it keeps adding 8 blocks at a time when it needs exta memory
