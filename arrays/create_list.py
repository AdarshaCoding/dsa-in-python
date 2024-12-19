import ctypes

class myList:
    def __init__(self):
        self.size = 1
        self.n = 0
        # create a C type array with size = self.size
        self.A = self.__make__array(self.size)
        
    def __make__array(self, capacity):
        # create c type array(static and referential) with size capacity
        return (capacity * ctypes.py_object)()
    
    def __len__(self):
        return self.n
    
L = myList()
print(L)
print(len(L))    