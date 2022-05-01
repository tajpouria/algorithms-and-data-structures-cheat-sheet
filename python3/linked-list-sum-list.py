class Node:
    next = None
    def __init__(self, data):
        self.data = data

def sum_list(c):
    if not c: return 0
    return c.data + sum_list(c.next)

a = Node(2)
b = Node(8)
c = Node(3)
d = Node(-1)
e = Node(7)

a.next = b
b.next = c
c.next = d
d.next = e

# 2 -> 8 -> 3 -> -1 -> 7

print(sum_list(a)) # 19

x = Node(38)
y = Node(4)

x.next = y

# 38 -> 4

print(sum_list(x)) # 42

z = Node(100)

# 100

print(sum_list(z)) # 100

print(sum_list(None)) # 0

