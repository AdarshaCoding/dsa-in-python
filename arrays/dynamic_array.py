import ctypes

lst = [1, 2, 3, 4]
print(lst)


class my_list:
    def __init__(self):
        self.size = 1
        self.n = 0
        # create a C type array with size = self.size
        self.A = self.__make_array(self.size)

    # length of the array
    def __len__(self):
        return self.n

    # print array values: print(array_name), used magic method __str__
    def __str__(self):
        result = ""
        for i in range(self.n):
            result = result + str(self.A[i]) + ", "

        return "[" + result[:-2] + "]"

    def __make_array(self, capacity):
        # c code to create an array (static and referential) with given size
        return (capacity * ctypes.py_object)()  # Immediately invoked

    def __resize(self, new_capacity):
        # create a new array with new cap acity
        B = self.__make_array(new_capacity)
        self.size = new_capacity
        # copy the content from A to B
        for i in range(self.n):
            B[i] = self.A[i]
        # re-assign to A
        self.A = B

    def append(self, item):
        if self.size == self.n:
            # resize the array
            self.__resize(self.size * 2)
        # append
        self.A[self.n] = item
        self.n = self.n + 1


L = my_list()

L.append(10)
L.append(20)
L.append("Hello")
L.append("World")
print(len(L))
print(L)
