# https://structy.net/problems/undirected-path

from collections import defaultdict, deque

def undirectedPath(edges, src, n):
    g = defaultdict(list)
    for n1, n2 in edges:
        g[n1].append(n2)
        g[n2].append(n1)

    vi = {}
    s = deque([src])
    while(len(s)):
        c = s.pop()
        if c == n:
            return True
        vi[c] = True
        for ne in g.get(c):
            if not vi.get(ne): s.append(ne)
    
    return False

edges = [
  ['i', 'j'],
  ['k', 'i'],
  ['m', 'k'],
  ['k', 'l'],
  ['o', 'n']
]

print(undirectedPath(edges, 'j', 'm')); # -> true

