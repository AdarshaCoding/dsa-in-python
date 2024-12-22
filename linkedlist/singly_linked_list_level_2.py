class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.n = 0

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.n = self.n + 1
            return
        new_node.next = self.head
        self.head = new_node
        self.n = self.n + 1

    def reverse_list(self):
        if self.head is None:
            print("The lis is empty!")
            return
        prev = None
        current = self.head
        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        self.head = prev

    def print_list(self):
        if self.head is None:
            print("The list is empty")
            return
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


ll = SinglyLinkedList()
ll.insert_at_beginning(10)
ll.insert_at_beginning(20)
ll.insert_at_beginning(30)
ll.insert_at_beginning(40)
ll.insert_at_beginning(50)

ll.print_list()
ll.reverse_list()
ll.print_list()


# Intermediate Problems:
# Reverse a Linked List:

# Reverse the linked list in place.
# Find Middle Node:

# Write a function to find the middle element of a linked list.
# Detect a Loop:

# Implement a function to detect if there is a cycle in the linked list.
# Remove Duplicates:

# Remove duplicate nodes from a sorted or unsorted linked list.
# Find Nth Node from End:

# Write a function to find the Nth node from the end of the linked list.
