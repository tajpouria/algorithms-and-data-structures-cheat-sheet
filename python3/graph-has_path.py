# https://structy.net/problems/has-path

from collections import deque

def has_path(g, src, n):
  s = deque([src])
  while len(s):
    c = s.pop()
    if c == n:
      return True
    for el in g.get(c):
      s.append(el)

  return False
 
def has_path_bfs(g, src, n):
  q = deque([src])
  while len(q):
    c = q.popleft()
    if c == n:
      return True
    for el in g.get(c):
      q.append(el)

  return False

g = {
  "f": ["g", "i"],
  "g": ["h"],
  "h": [],
  "i": ["g", "k"],
  "j": ["i"],
  "k": [],
}

print(has_path(g, "f", "k")) # True
print(has_path_bfs(g, "f", "k")) # True

