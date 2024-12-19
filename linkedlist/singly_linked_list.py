class Node:
    def __init__(self, value):
        self.value = value  # value
        self.next = None  # reference or pointer


# Singly Linked List
class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.n = 0

    # checks if list is empty
    def is_empty(self):
        if self.head is None:
            return True

    def size(self):
        return self.n

    # insert a node at the end
    def insert_at_end(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.head = new_node
            self.n += 1
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        self.n += 1

    def insert_at_beginning(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self.n += 1

    def insert_after(self, after, value):
        new_node = Node(value)
        current = self.head
        while current != None:
            if current.value == after:
                break
            current = current.next

        if current != None:
            new_node.next = current.next
            current.next = new_node
            self.n = self.n + 1
        else:
            print(f"Node {after} not found!")

        # if position < 0:
        #     raise IndexError("Position is not correct!")

        # if position == 0:
        #     new_node.next = self.head
        #     self.head = new_node
        #     self.n += 1
        #     return

        # current = self.head
        # current_position = 1
        # while current and current_position < position - 1:
        #     current_position += 1
        #     current = current.next

        # if current is None:
        #     print("Position is out of bounds.")
        #     return

        # new_node.next = current.next
        # current.next = new_node
        # self.n += 1

    # display all the node from the list
    def display(self):
        result = []
        current = self.head
        while current:
            result.append(str(current.value))
            current = current.next
        print(" -> ".join(result), end=" -> None")


ll = SinglyLinkedList()
ll.insert_at_end(10)
ll.insert_at_end(20)
ll.insert_at_end(30)
ll.insert_at_beginning(70)
# ll.insert_at_beginning(0)
# ll.insert_at_position(2, 40)
ll.insert_after(66, 88)
ll.display()
print("\nLength of the linked list: ", ll.size())
