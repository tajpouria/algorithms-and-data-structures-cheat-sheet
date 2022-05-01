class Node:
    next = None

    def __init__(self, data):
       self.data = data

def linked_list_values(c):
    if not c: return []
    return [c.data] + linked_list_values(c.next)


a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")

a.next = b
b.next = c
c.next = d

# a -> b -> c -> d

print(linked_list_values(a)) # -> [ 'a', 'b', 'c', 'd' ]

x = Node("x")
y = Node("y")

x.next = y

# x -> y

print(linked_list_values(x)) # -> [ 'x', 'y' ]

q = Node("q")

# q

print(linked_list_values(q)) # -> [ 'q' ]

print(linked_list_values(None)) # -> [ ]

