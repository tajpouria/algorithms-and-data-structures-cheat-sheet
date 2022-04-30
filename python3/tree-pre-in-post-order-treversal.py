class Node:
    left = None
    right = None
    def __init__(self, data):
        self.data = data


def pre_order_traversal(c):
    tr = [c.data]
    if c.left: tr += pre_order_traversal(c.left)
    if c.right: tr += pre_order_traversal(c.right)
    return tr

def in_order_traversal(c):
    tr = [c.data]
    if c.left: tr = in_order_traversal(c.left) + tr
    if c.right: tr += in_order_traversal(c.right)
    return tr

def post_order_traversal(c):
    tr = []
    if c.left: tr += post_order_traversal(c.left)
    if c.right: tr += post_order_traversal(c.right)
    tr += [c.data]
    return tr

a = Node(-1)
b = Node(-6)
c = Node(-5)
d = Node(-3)
e = Node(0)
f = Node(-13)
g = Node(-1)
h = Node(-2)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
e.left = g
f.right = h

#        -1
#      /   \
#    -6    -5
#   /  \     \
# -3   0    -13
#     /       \
#    -1       -2

# Depth first traversal:
# pre order: root, left, right
# in order: left, root, right
# post order: left, right, root
# 
# Breadth first traversal
# Level

print(f"pre-order: {pre_order_traversal(a)}") # [-1, -6, -3, 0, -1, -5, -13, -2] # [-1, -6, -3, 0, -1, -5, -13, -2]
print(f"in-order: {in_order_traversal(a)}") # [-3, -6, -1, 0, -1, -5, -13, -2] # [-3, -6, -1, 0, -1, -5, -13, -2] 
print(f"post-order: {post_order_traversal(a)}") # [-3, -1, 0, -6, -2, -13, -5, -1] # [-3, -1, 0, -6, -2, -13, -5, -1]
