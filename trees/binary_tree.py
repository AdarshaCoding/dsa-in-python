class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)


A = TreeNode(10)
B = TreeNode(7)
C = TreeNode(12)
D = TreeNode(5)
E = TreeNode(9)
G = TreeNode(15)
H = TreeNode(11)

A.left = B
A.right = C
B.left = D
B.right = E
C.right = G
C.left = H


# DFS - Recursive
# DSF: Pre-Order (Node|Left|Right) - NLR
def pre_order(node):
    if node:
        print(node.data, end=" ")
        pre_order(node.left)
        pre_order(node.right)


print("Pre-Order Traversal: ")
pre_order(A)


# DSF: Pre-Order Iterative (Node|Left|Right) - NLR | Using Stack
def pre_order_iterative(node):
    stk = [node]
    while stk:
        node = stk.pop()
        print(node, end=" ")
        if node.right:
            stk.append(node.right)
        if node.left:
            stk.append(node.left)


print("\nPre Order Iterative: ")
pre_order_iterative(A)

# BFS : Level Order Traversal - Using Queues
from collections import deque


def level_order(node):
    q = deque()
    q.append(node)

    while q:
        node = q.popleft()
        print(node, end=" ")
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)


print("\nLevel Order Traversal: ")
level_order(A)


# Normal search in a Binary Tree
def search(node, target):
    if not node:
        return False

    if node.data == target:
        return True

    return search(node.left, target) or search(node.right, target)


print("\n", search(A, 22))

# Search in BST : Binary Search Tree


def search_bst(node, target):
    if not node:
        return False
    if node.data == target:
        return True
    if target < node.data:
        return search_bst(node.left, target)
    else:
        return search_bst(node.right, target)


print(search_bst(A, 9))
