def invert_binary_tree(c):
	if not c:
		return None
	c.left, c.right = c.right, c.left
	invert_binary_tree(c.left)
	invert_binary_tree(c.right)

