import ctypes


class MyList:
    def __init__(self):
        self.size = 1
        self.n = 0
        # create c-type array with self.size
        self.A = self.__make_array(self.size)

    # magic method
    def __len__(self):
        return self.n

    def __getitem__(self, index):
        if 0 <= index < self.n:
            return self.A[index]
        else:
            return "IndexError - Index Out Of Range!"

    def __str__(self):
        result = ""
        for i in range(self.n):
            if isinstance(self.A[i], str):
                result = result + "'" + str(self.A[i]) + "'" + ", "
            else:
                result = result + str(self.A[i]) + ", "
        return "[" + result[:-2] + "]"

    def __delitem__(self, pos):
        if (
            0 <= pos < self.n
        ):  # else it will delete the last element if pos is more than the self.n
            for i in range(pos, self.n - 1):
                self.A[i] = self.A[i + 1]
            self.n = self.n - 1

    def append(self, item):
        if self.n == self.size:  # no vacant place to add the item into array
            # resize the array
            self.__resize(self.size * 2)

        # append
        self.A[self.n] = item
        self.n = self.n + 1

    def __resize(self, new_capacity):
        # create a new array with new capacity
        B = self.__make_array(new_capacity)
        self.size = new_capacity

        # copy the content of A to B (new array B will have more place to store now)
        for i in range(self.n):
            B[i] = self.A[i]
        # reassign A
        self.A = B

    def __make_array(self, capacity):
        # it creates c-type array (static, referential) with provided capacity/size
        return (capacity * ctypes.py_object)()

    def pop(self):
        if self.n == 0:
            return "List is empty"
        last_item = self.A[self.n - 1]
        self.n = self.n - 1
        return last_item

    def clear(self):
        self.size = 1
        self.n = 0

    def find(self, item):
        if self.n == 0:
            return "List is empty!"
        for i in range(self.n):
            if item == self.A[i]:
                return True
        return False

    def insert(self, pos, item):
        if self.size == self.n:
            self.__resize(self.size * 2)
        for i in range(self.n, pos, -1):
            self.A[i] = self.A[i - 1]
        self.A[pos] = item
        self.n = self.n + 1

    def print_list(self):
        for i in range(self.n):
            print(type(self.A[i]), end=", ")
            if isinstance(self.A[i], int):
                print(self.A[i])


L = MyList()
L.append(10)
L.append("Hello World")
L.append(3.4)
L.append(True)
L.append("Adarsha")
L.append({"a": "Adarsha", 1: "Deepa"})
print(len(L))
print(L)
L.print_list()
print(L[-1])
print(L.pop())
# L.clear()
# print(len(L))
print(L.find(100))
L.insert(0, 456)
print(L)
L.insert(2, 789)
print(L)
del L[100]
print(L)


# sort/min/max/sum
# extend
# negative indexing
# slicing
# merge
