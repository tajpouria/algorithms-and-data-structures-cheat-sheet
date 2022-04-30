class Node():
    left = None
    right = None

    def __init__(self, data):
        self.data = data

def tree_sum(c):
    if not c: return 0

    acc = c.data
    if c.left: acc += tree_sum(c.left)
    if c.right: acc += tree_sum(c.right)

    return acc

        

a = Node(3)
b = Node(11)
c = Node(4)
d = Node(4)
e = Node(-2)
f = Node(1)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

#       3
#    /    \
#   11     4
#  / \      \
# 4   -2     1

print(tree_sum(a)) # -> 21

a = Node(1)
b = Node(6)
c = Node(0)
d = Node(3)
e = Node(-6)
f = Node(2)
g = Node(2)
h = Node(2)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
e.left = g
f.right = h

#      1
#    /   \
#   6     0
#  / \     \
# 3   -6    2
#    /       \
#   2         2

print(tree_sum(a)) # -> 10

print(tree_sum(None)) # -> 0

