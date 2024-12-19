class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


a = Node(10)
b = Node(20)
c = Node(30)

print(f"a: {id(a)}, b: {id(b)}, c: {id(c)}")

a.next = b
b.next = c

print(f"a -> b : {id(a.next)}")
print(f"b -> c : {id(b.next)}")
print(f"c -> {c.next}")
