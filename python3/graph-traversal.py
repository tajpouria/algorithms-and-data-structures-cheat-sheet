from collections import deque

def depth_first_search(g, src):
  s = deque([src])
  
  while len(s):
    c = s.pop()
    print(c, end="")
    for el in g.get(c):
      s.append(el)

def depth_first_search_recursion(g, src):
  print(src, end="")
  for n in g.get(src):
    depth_first_search_recursion(g, n)  

def breadth_first_search(g, src):
  q = deque([src])
  while len(q):
    c = q.popleft()
    print(c, end="")
    for el in g.get(c):
      q.append(el)

g = {
  'a': ['b', 'c'],
  'b': ['d'],
  'c': ['e'],
  'd': ['f'],
  'e': [],
  'f': []
 }

depth_first_search(g, 'a')
print("")
depth_first_search_recursion(g, 'a')
print("")
breadth_first_search(g, 'a')

