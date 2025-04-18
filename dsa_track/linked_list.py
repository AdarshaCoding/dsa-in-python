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

    def clear(self):
        if self.head:
            self.head = None
            self.n = 0

    def delete_at_start(self):
        if self.head is None:
            print("The list is empty!")
            return
        self.head = self.head.next
        self.n = self.n - 1

    def delete_at_last(self):
        if self.head is None:
            print("The list is empty!")
            return
        current = self.head
        if current.next == None:
            return self.delete_at_start()

        while current.next.next != None:
            current = current.next

        current.next = None
        self.n = self.n - 1

    def delete_by_value(self, value):
        if self.head is None:
            print("The list is empty!")
            return
        if self.head.data == value:
            return self.delete_at_start()

        current = self.head

        while current.next:
            if current.next.data == value:
                break
            current = current.next
        if current is None:
            print("The target value not found!")
        else:
            current.next = current.next.next
            self.n = self.n - 1

    def search_by_value(self, value):
        if self.head is None:
            print("The list is empty!")
            return
        current = self.head
        pos = 0
        while current:
            if current.data == value:
                return pos
            current = current.next
            pos = pos + 1

    def __getitem__(self, index):
        # if pos < 0:
        #     print("Provided position is not correct!")
        #     return
        if self.head is None:
            print("The list is empty!")
            return

        pos = 0
        current = self.head
        while current:
            if pos == index:
                return current.data
            current = current.next
            pos = pos + 1
        return "Postion is not valid"

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
ll.insert_at_beginning(50)
ll.insert_at_beginning(60)
# ll.insert_at_end(100)
# ll.insert_at_end(500)
ll.print_list()
print(len(ll))
print(ll.search_by_value(10))
print(ll[0])

# ll.insert_after(100, 66)
# ll.print_list()
# print(len(ll))
# print("delete start")
# ll.delete_at_start()
# ll.print_list()
# print(len(ll))
# print("Delete at last")
# ll.delete_at_last()
# ll.delete_at_last()
# ll.delete_at_last()
# ll.delete_at_last()
# ll.print_list()
# print(len(ll))
# print("delete by value")
# ll.delete_by_value(30)
# ll.print_list()
# print(len(ll))
# print("clear")
# ll.clear()
# ll.print_list()
# print(len(ll))
