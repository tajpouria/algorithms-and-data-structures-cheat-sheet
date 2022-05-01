class Node:
	nxt = None
	def __init__(self, data):
		self.data = data


def traverse(h):
	c = h
	while c:
		print(c.data)
		c = c.nxt

def traverse_recursion(c):
	if not c: return
	print(c.data)
	traverse_recursion(c.nxt)


a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')

a.nxt = b
b.nxt = c
c.nxt = d
d.nxt = e

traverse(a)
print('---')
traverse_recursion(a)

