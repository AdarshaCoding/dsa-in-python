class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None


def has_cycle(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True
    return False


A = ListNode(10)
B = ListNode(20)
C = ListNode(30)
D = ListNode(40)
E = ListNode(50)

A.next = B
B.next = C
C.next = D
D.next = E
E.next = A  # If there is no connection from E --> A then "No Cycle"

print(has_cycle(A))
