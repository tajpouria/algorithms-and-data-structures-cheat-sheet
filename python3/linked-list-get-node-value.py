class Node:
    next = None
    def __init__(self, data):
        self.data = data


def get_node_value(c, i):
    j = 0
    cn = c
    while j < i:
        if not cn: return None
        cn = cn.next
        j += 1

    return cn.data if cn else None

a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")

a.next = b
b.next = c
c.next = d

# a -> b -> c -> d

print(get_node_value(a, 2)) # 'c'


a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")

a.next = b
b.next = c
c.next = d

# a -> b -> c -> d

print(get_node_value(a, 3)) # 'd'

a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")

a.next = b
b.next = c
c.next = d

# a -> b -> c -> d

print(get_node_value(a, 7)) # None

node1 = Node("banana")
node2 = Node("mango")

node1.next = node2

# banana -> mango

print(get_node_value(node1, 0)) # 'banana'

node1 = Node("banana")
node2 = Node("mango")

node1.next = node2

# banana -> mango

print(get_node_value(node1, 1)) # 'mango'
