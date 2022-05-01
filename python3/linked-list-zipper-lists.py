class Node:
    next = None
    def __init__(self, data):
        self.data = data

def zipper_lists(h1, h2):
    while h1 and h2:
        h1n = h1.next
        h2n = h2.next
        h1.next = h2
        if h1n: h2.next = h1n
        h1 = h1n
        h2 = h2n

def print_list(h):
    while h:
        print(h.data)
        h = h.next


a = Node("a")
b = Node("b")
c = Node("c")
a.next = b
b.next = c
# a -> b -> c 

x = Node("x")
y = Node("y")
z = Node("z")
x.next = y
y.next = z
# x -> y -> z

zipper_lists(a, x)
print_list(a)
print('---')
# a -> x -> b -> y -> c -> z

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

x = Node("x")
y = Node("y")
z = Node("z")
x.next = y
y.next = z
# x -> y -> z

zipper_lists(a, x)
print_list(a)
print('---')
# a -> x -> b -> y -> c -> z -> d -> e -> f

s = Node("s")
t = Node("t")
s.next = t
# s -> t

one = Node(1)
two = Node(2)
three = Node(3)
four = Node(4)
one.next = two
two.next = three
three.next = four
# 1 -> 2 -> 3 -> 4

zipper_lists(s, one)
print_list(s)
print('---')
# s -> 1 -> t -> 2 -> 3 -> 4

w = Node("w")
# w

one = Node(1)
two = Node(2)
three = Node(3)
one.next = two
two.next = three
# 1 -> 2 -> 3

zipper_lists(w, one)
print_list(w)
print('---')
# w -> 1 -> 2 -> 3

one = Node(1)
two = Node(2)
three = Node(3)
one.next = two
two.next = three
# 1 -> 2 -> 3

w = Node("w")
# w

zipper_lists(one, w)
print_list(one)
print('---')
# 1 -> w -> 2 -> 3

