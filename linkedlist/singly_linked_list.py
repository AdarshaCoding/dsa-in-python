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
        current = self.head


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
