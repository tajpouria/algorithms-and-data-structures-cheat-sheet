from collections import defaultdict, deque

def shortest_path(e, src, dest):
    g = defaultdict(list)
    for n1, n2 in e:
        g[n1].append(n2)
        g[n2].append(n1)

    q = deque([(src, 0)])
    vi = {}
    while(len(q)):
        (c, dist) = q.popleft()
        if c == dest: return dist 
        vi[c] = True
        for ne in g.get(c):
            if not vi.get(ne): q.append((ne, dist + 1))

    return -1

edges = [
  ['w', 'x'],
  ['x', 'y'],
  ['z', 'y'],
  ['z', 'v'],
  ['w', 'v']
]

print(shortest_path(edges, 'w', 'z')) # -> 2

edges = [
  ['m', 'n'],
  ['n', 'o'],
  ['o', 'p'],
  ['p', 'q'],
  ['t', 'o'],
  ['r', 'q'],
  ['r', 's']
]

print(shortest_path(edges, 'm', 's')) # -> 

edges = [
    ['a', 'c'],
    ['a', 'b'],
    ['c', 'b'],
    ['c', 'd'],
    ['b', 'd'],
    ['e', 'd'],
    ['g', 'f']
]

print(shortest_path(edges, 'b', 'g')) # -> -1

