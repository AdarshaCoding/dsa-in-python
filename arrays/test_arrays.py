import array as arr

arr1 = arr.array("I", [1,2,3,4,5])
arr2 = arr.array("u", ["a", "b", "c"])
print(arr1)
for el in arr1:
    print(el)

for ch in arr2:
    print(ch, end=" ")