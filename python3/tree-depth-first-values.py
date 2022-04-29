from collections import deque

class Node:
	left = None
	right = None

	def __str__(self):
		return str(self.data)

	def __init__(self, data):
		self.data = data

def depth_first_values(r):
	s = deque([r])
	res = []
	while len(s):
		c = s.pop()
		if not c: continue
		if type(c.data) is str: res.append(c.data)
		if c.right: s.append(c.right)
		if c.left: s.append(c.left)
			
	return res

def depth_first_values_recursion(c):
	if not c: return []
	res = [c.data]
	if c.left: res += depth_first_values(c.left)
	if c.right: res += depth_first_values(c.right)

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

print(depth_first_values(a))
print("Recursion", depth_first_values_recursion(a))
#   -> ['a', 'b', 'd', 'e', 'c', 'f']

a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')
g = Node('g')
a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
e.left = g

#      a
#    /   #   b     c
#  / \     # d   e     f
#    /
#   g

print(depth_first_values(a))
#   -> ['a', 'b', 'd', 'e', 'g', 'c', 'f']

a = Node('a')
#     a
print(depth_first_values(a)) 
#   -> ['a']

a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
a.right = b;
b.left = c;
c.right = d;
d.right = e;

#      a
#       #        b
#       /
#      c
#       #        d
#         #          e

print(depth_first_values(a)) 
#   -> ['a', 'b', 'c', 'd', 'e']

print(depth_first_values(None)) 
#   -> []
