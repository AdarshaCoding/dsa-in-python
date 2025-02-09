class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.n = 0

    def __len__(self):
        return self.n

    def __str__(self):
        current = self.head
        result = ""
        while current:
            result = result + str(current.data) + " -> "
            current = current.next
        return result + "None"

    def append(self, data):
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

    def reverse(self):
        if self.head is None:
            print("The list is empty!")
            return
        prev = None
        current = self.head
        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        self.head = prev

    def sum_of_odd_positions(self):
        pos = 0
        sum = 0
        current = self.head
        while current:
            if pos % 2 != 0:
                sum = sum + current.data
            pos = pos + 1
            current = current.next
        print(sum)

    def remove_duplicate(self):
        pass


arr = [10, 20, 30, 40, 50]
ll = LinkedList()
for el in arr:
    ll.append(el)
print(ll)
ll.reverse()
print(ll)
ll.sum_of_odd_positions()
