from collections import deque


class Node:
	left = None
	right = None
	def __init__(self, data):
		self.data = data

def dfs(a, t):
	if a.data == t: return True

	lr, rr = False, False
	if(a.left): lr = dfs(a.left, t)
	if(a.right): rr = dfs(a.right, t)

	return lr or rr

def bfs(a, t):
	q = deque([a])
	while(len(q)):
		c = q.popleft()
		if c.data == t: return True
		if(c.left): q.append(c.left)
		if(c.right): q.append(c.right)

	return False
			

def tree_includes(a, t, use_recursion=True):
	if not use_recursion:
		return bfs(a, t)
	
	return dfs(a, t)

a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

#      a
#    /   #   b     c
#  / \     # d   e     f

print(tree_includes(a, "e", use_recursion=False)) # -> True

a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

#      a
#    /   #   b     c
#  / \     # d   e     f
tree_includes(a, "a") # -> True

a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

#      a
#    /   #   b     c
#  / \     # d   e     f

print(tree_includes(a, "n")) # -> False

a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")
g = Node("g")
h = Node("h")

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

print(tree_includes(a, "f")) # -> True

a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")
g = Node("g")
h = Node("h")

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

print(tree_includes(a, "p")) # -> False
