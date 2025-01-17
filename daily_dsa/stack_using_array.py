class Stack:
    def __init__(self):
        self.stk = []

    def push(self, data):
        self.stk.append(data)

    def is_empty(self):
        return len(self.stk) == 0

    def peek(self):
        if self.is_empty():
            print("Stack is empty!")
            return
        return self.stk[-1]

    def pop(self):
        if self.is_empty():
            print("Stack is empty!")
            return
        return self.stk.pop()

    def display(self):
        print(self.stk)

    def size(self):
        return len(self.stk)

    # def __len__(self):
    #     return len(self.stk)


stk = Stack()
print(stk.is_empty())
stk.peek()
stk.pop()

stk.push(10)
stk.push(20)
stk.push(30)
stk.push(40)

stk.display()
stk.pop()
stk.display()
print(stk.size())
print(len(stk))
