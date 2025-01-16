# Day_2 - 16/01/2025
# 3. Implement a stack using arrays/linked list.


# Node class with data and the pointer to the next element in the stack
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.is_empty():
            print("Stack is underflow!")
            return
        else:
            data = self.top.data
            self.top = self.top.next
            return data

    def peek(self):
        if self.is_empty():
            print("Stack is empty!")
            return None
        return self.top.data

    def display(self):
        if self.is_empty():
            print("Stack is empty!")
        else:
            current = self.top
            print("Stack elements:", end=" ")
            while current:
                print(current.data, end=" ")
                current = current.next
            print()


# Constant time complexity (O(1)) for push, pop, and peek operations.
stack = Stack()
stack.peek()
stack.display()
value = stack.pop()
print(value)
stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)
stack.display()
value = stack.pop()
print(value)
stack.display()
