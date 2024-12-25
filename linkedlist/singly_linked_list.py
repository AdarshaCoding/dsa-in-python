# individual node blueprint
class Node:
    def __init__(self, data):
        self.data = data  # data
        self.next = None  # pointer to next node

    def __str__(self) -> str:
        return str(self.data)


# create a list with more node
class SinglyLinkedList:
    def __init__(self):
        self.head = None  # start with empty head
        self.n = 0

    def __len__(self):
        return self.n

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.n = self.n + 1
            return
        new_node.next = self.head
        self.head = new_node
        self.n = self.n + 1

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.n = self.n + 1
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        self.n = self.n + 1

    def insert_after(self, target, data):
        if self.head is None:
            print("The list is empty and dosn'e contain any target value")
            return
        current = self.head
        while current:
            if current.data == target:
                break
            current = current.next
        if current is None:
            print("The target value is not found!")
        else:
            new_node = Node(data)
            new_node.next = current.next
            current.next = new_node
            self.n = self.n + 1

    def delete_at_start(self):
        if self.head is None:
            print("The list is already empty!")
            return
        self.head = self.head.next
        self.n = self.n - 1

    def delete_at_end(self):
        if self.head is None:
            print("The list is already empty!")
            return
        current = self.head
        while current.next.next:  # current.next.next is not None
            current = current.next
        current.next = None
        self.n = self.n - 1

    def delete_by_value(self, value):
        if self.head is None:
            print("The list is already empty!")
            return
        if self.head.data == value:
            self.head = self.head.next
            self.n = self.n - 1
            return
        current = self.head
        while current.next:
            if current.next.data == value:
                break
            current = current.next

        if current is None:
            print("The value is not found in the list!")
            return

        current.next = current.next.next
        self.n = self.n - 1

    def reverse(self):
        if self.head is None:
            print("The list is empty")
            return
        if self.head.next is None:
            print("There is only one element in the list!")
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
            print("The list is empty!")
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

ll.insert_at_end(77)

ll.insert_after(30, 33)

ll.print_list()

ll.delete_at_end()
ll.print_list()

ll.delete_at_start()
ll.print_list()

ll.delete_by_value(33)
ll.print_list()

ll.reverse()
print("Reversed list: ")
ll.print_list()

print("Length of the linked list: ", len(ll))
