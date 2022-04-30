from collections import deque

class Node:
    left = None 
    right = None

    def __init__(self, data):
        self.data = data 

def breadth_first_values(r):
	q = deque([r])
	res = []
	while(len(q)):
		c = q.popleft()
		if not c: break
		res.append(c.data)
		if c.left: q.append(c.left)
		if c.right: q.append(c.right)

	return res


a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

#      a
#    /   #   b     c
#  / \     # d   e     f

print(breadth_first_values(a)) 
#    -> ['a', 'b', 'c', 'd', 'e', 'f']

a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')
g = Node('g')
h = Node('h')

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
e.left = g
f.right = h

#      a
#    /   #   b     c
#  / \     # d   e     f
#    /       #   g         h

print(breadth_first_values(a)) 
#   -> ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

a = Node('a')

#      a

print(breadth_first_values(a)) 
#    -> ['a']

a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
x = Node('x')

a.right = b
b.left = c
c.left = x
c.right = d
d.right = e

#      a
#       #        b
#       /
#      c
#    /  #   x    d
#         #          e

print(breadth_first_values(a)) 
#    -> ['a', 'b', 'c', 'x', 'd', 'e']

print(breadth_first_values(None)) 
#    -> []
