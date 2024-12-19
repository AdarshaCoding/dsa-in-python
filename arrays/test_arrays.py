class Stack:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return len(self.items) == 0
    
    def add(self, value):
        self.items.append(value)
    
    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        
        return self.stk.pop()
        
    def peek(self):
        return self.items[-1]

stk = Stack()
stk.add(10)
stk.add(20)
print(stk)
