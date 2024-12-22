class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.n = 0

    def __len__(self):
        return self.n

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            self.n = self.n + 1
            return
        new_node.next = self.head
        self.head = new_node
        self.n = self.n + 1

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            self.n = self.n + 1
            return
        current = self.head
        while current.next != None:
            current = current.next
        current.next = new_node
        self.n = self.n + 1

    def insert_after(self, key_value, data):
        if self.head == None:
            return "List is empty"
        new_node = Node(data)
        current = self.head
        while current:
            if current.data == key_value:
                break
            current = current.next

        if current is None:
            print("Key value not found!")
            return

        new_node.next = current.next
        current.next = new_node
        self.n = self.n + 1

    def search(self, value):
        position = 0
        if self.head is None:
            return None
        if self.head.data == value:
            return position
        current = self.head
        while current != None:
            if current.data == value:
                return position
            position = position + 1
            current = current.next

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def reverse_list(self):
        prev = None
        current = self.head
        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        self.head = prev

    def delete_by_value(self, value):
        if self.head is None:
            return "List is empty!"
        if self.head.data == value:
            self.head = self.head.next
            return

        current = self.head
        while current.next != None:
            if current.next.data == value:
                break
            current = current.next

        if current is None:
            print("Enter value is not correct")
            return
        current.next = current.next.next
        self.n = self.n - 1


ll = SinglyLinkedList()
ll.insert_at_end(10)
ll.insert_at_end(20)
ll.insert_at_end(30)
ll.insert_at_end(40)
ll.insert_after(30, 77)
ll.insert_at_beginning(66)

ll.print_list()
# ll.reverse_list()
# ll.print_list()

print("Position: " + str(ll.search(40)))
print(len(ll))
ll.delete_by_value(40)
ll.print_list()
print(len(ll))

# Beginner Problems:
# Create a Linked List:

# Write a function to create a linked list from a list of elements.
# Display Linked List:

# Implement a function to traverse and print all elements in the linked list.
# Search an Element:

# Write a function to search for an element in a linked list and return its position (or None if not found).
# Count Nodes:

# Write a function to count the number of nodes in a linked list.
# Delete a Node:

# Implement a function to delete a node by value in a linked list.
