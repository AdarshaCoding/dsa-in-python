# Day_1 - 15/01/2025
# 1. Reverse a linked list.
# 2. Find the middle element of a linked list.


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Insert at the beginning
    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        new_node.next = self.head
        self.head = new_node

    # Print all the node
    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    # Reverse the linked list
    def reverse(self):
        current = self.head
        prev = None
        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        self.head = prev

    # 70 -> 60 -> 50 -> 40 -> 30 -> 20 -> 10 -> None
    # 10 -> 20 -> 30 -> 40 -> 50 -> 60 -> 70 -> None

    # 1st iteration:
    # temp =  60 -> 50 -> 40 -> 30 -> 20 -> 10 -> None
    # current.next = None ->  70-None
    # prev = 70-None
    # current = 60 -> 50 -> 40 -> 30 -> 20 -> 10 -> None
    # 2nd iteration
    # temp =  50 -> 40 -> 30 -> 20 -> 10 -> None
    # current.next = 60-Next --> 70-None
    # prev = 60--> 70--> None
    # current = 50 -> 40 -> 30 -> 20 -> 10 -> None

    # find the middle element in the list
    def find_middle_element(self):
        if self.head is None:
            print("The list is empty")
            return

        current = self.head
        count = 1
        while current:
            count += 1
            current = current.next

        if count > 1:
            mid = count // 2
            print("Middle Index: ", mid)

        current = self.head
        count = 1
        while current:
            if count == mid:
                print(current.data)
                break
            current = current.next
            count += 1


ll = LinkedList()
ll.insert_at_beginning(10)
ll.insert_at_beginning(20)
ll.insert_at_beginning(30)
ll.insert_at_beginning(40)
ll.insert_at_beginning(50)
ll.insert_at_beginning(60)
ll.insert_at_beginning(70)

ll.print_list()
ll.reverse()
ll.print_list()
ll.find_middle_element()
