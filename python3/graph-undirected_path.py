# https://structy.net/problems/undirected-path

from collections import defaultdict

def to_adj_list(e):
  g = defaultdict(list)
  for rel in edges:
    n1, n2 = rel
    g[n1].append(n2)
    g[n2].append(n1)
  
  return g

edges = [
  ["i", "j"],
  ["k", "i"],
  ["m", "k"],
  ["k", "l"],
  ["o", "n"],
]

g = to_adj_list(edges)
print(g)

