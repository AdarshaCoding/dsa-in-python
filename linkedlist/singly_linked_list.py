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

# Output
# a: 2159175951872, b: 2159175951920, c: 2159175952016
# a -> b : 2159175951920
# b -> c : 2159175952016
# c -> None
