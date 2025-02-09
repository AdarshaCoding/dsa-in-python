class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None  # Empty list
        self.n = 0  # No. of nodes in LL

    def __len__(self):
        return self.n

    def insert_at_beginning(self, data):
        # create new node
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.n = self.n + 1
            return
        # create connection
        new_node.next = self.head
        # reassign head
        self.head = new_node
        # increment no. of node
        self.n = self.n + 1

    def insert_at_end(self, data):
        new_node = Node(data)

        if self.head is None:
            # list is empty
            self.head = new_node
            self.n = self.n + 1
            return
        # traverse till last node
        current = self.head
        while current.next != None:
            current = current.next

        # we are at the last node
        current.next = new_node
        self.n = self.n + 1

    def insert_after(self, value, data):
        new_node = Node(data)

        if self.head is None:
            print("The list is empty!")
            return
        current = self.head
        while current:
            if current.data == value:
                break
            current = current.next

        if current is None:
            print("The target value is not found!")
        else:
            # maintain this order of assignment of nodes else it would end up in infinite loop
            new_node.next = current.next
            current.next = new_node
            self.n = self.n + 1

    # traverse list
    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


ll = SinglyLinkedList()

ll.insert_at_beginning(10)
ll.insert_at_beginning(30)
ll.insert_at_beginning(40)
ll.insert_at_end(100)
ll.insert_at_end(500)
ll.print_list()
print(len(ll))
ll.insert_after(100, 66)
ll.print_list()
print(len(ll))
