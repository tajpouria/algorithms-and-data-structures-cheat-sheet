class Node:
    next = None 
    def __init__(self, data):
        self.data = data

def linked_list_find(c, t):
   if not c: return False 
   return c.data == t or linked_list_find(c.next, t)

a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")

a.next = b
b.next = c
c.next = d

# a -> b -> c -> d

print(linked_list_find(a, "c")) # True

a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")

a.next = b
b.next = c
c.next = d

# a -> b -> c -> d

print(linked_list_find(a, "d")) # True

a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")

a.next = b
b.next = c
c.next = d

# a -> b -> c -> d

print(linked_list_find(a, "q")) # False

node1 = Node("jason")
node2 = Node("leneli")

node1.next = node2

# jason -> leneli

print(linked_list_find(node1, "jason")) # True

node1 = Node("jason")
node2 = Node("leneli")

node1.next = node2

# jason -> leneli

linked_list_find(node1, "jason") # True

node1 = Node(42)

# 42

print(linked_list_find(node1, 100)) # False

