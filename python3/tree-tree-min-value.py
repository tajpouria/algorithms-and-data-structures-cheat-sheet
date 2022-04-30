from collections import deque
from math import inf

class Node:
    left = None
    right = None

    def __init__(self, data):
        self.data = data
        

def tree_min_value(r):
    m = inf
    q = deque([r])
    while(len(q)):
       c = q.popleft() 
       m = min(c.data, m) 
       if c.left: q.append(c.left)
       if c.right: q.append(c.right)

    return m

def dft(c):
   m = c.data
   if c.left: m = min(m, dft(c.left))
   if c.right: m = min(m, dft(c.right))
   return m


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
print(tree_min_value(a)) # -> -2
print(dft(a)) # -> -2

a = Node(5)
b = Node(11)
c = Node(3)
d = Node(4)
e = Node(14)
f = Node(12)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

#       5
#    /    \
#   11     3
#  / \      \
# 4   14     12

print(tree_min_value(a)) # ->3

a = Node(-1)
b = Node(-6)
c = Node(-5)
d = Node(-3)
e = Node(-4)
f = Node(-13)
g = Node(-2)
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
# -3   -4   -13
#     /       \
#    -2       -2

print(tree_min_value(a)) # -> -13
print(dft(a)) # -> -13

a = Node(42)

#        42

print(tree_min_value(a)) # -> 42
