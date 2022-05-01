class Node:
    next = None
    def __init__(self, data):
        self.data = data

def reverse_list(r):
    c, p = r, None
    while c:
        n = c.next
        c.next = p
        p = c
        c = n

def print_list(r, pa=False):
    if not r: 
        print("")
        return
    if pa: print(" -> ", end="")
    print(r.data, end="")
    print_list(r.next, pa=True)


a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f

# a -> b -> c -> d -> e -> f

reverse_list(a) # f -> e -> d -> c -> b -> a
print_list(f)


x = Node("x")
y = Node("y")

x.next = y

# x -> y

reverse_list(x) # y -> x
print_list(y)

p = Node("p")

# p

reverse_list(p) # p
print_list(p)
