# https://structy.net/problems/island-count

def explore(g, ri, ci, vi):
    if not 0 <= ri < len(g): return False
    if not 0 <= ci < len(g[ri]): return False

    if g[ri][ci] == 'W': return False

    l = f"{ri},{ci}"
    if vi.get(l): return False
    vi[l] = 1

    explore(g, ri + 1, ci, vi)
    explore(g, ri - 1, ci, vi)
    explore(g, ri, ci + 1, vi)
    explore(g, ri, ci - 1, vi)

    return True


def island_count(g):
    res = 0
    vi = {}
    for ri in range(len(g)):
        for ci in range(len(g[ri])):
            # ri, ci
            # ri + 1, ci
            # ri - 1, ci
            # ri, ci + 1
            # ri, ci - 1
            if explore(g, ri, ci, vi): res += 1

    return res


grid = [
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'W', 'W', 'L', 'W'],
  ['W', 'W', 'L', 'L', 'W'],
  ['L', 'W', 'W', 'L', 'L'],
  ['L', 'L', 'W', 'W', 'W'],
]

print(island_count(grid)) # -> 3

grid = [
  ['L', 'W', 'W', 'L', 'W'],
  ['L', 'W', 'W', 'L', 'L'],
  ['W', 'L', 'W', 'L', 'W'],
  ['W', 'W', 'W', 'W', 'W'],
  ['W', 'W', 'L', 'L', 'L'],
]

print(island_count(grid)) # -> 4

grid = [
  ['L', 'L', 'L'],
  ['L', 'L', 'L'],
  ['L', 'L', 'L'],
]

print(island_count(grid)) # -> 1

grid = [
  ['L', 'L', 'L'],
  ['L', 'L', 'L'],
  ['L', 'L', 'L'],
]

print(island_count(grid)) # -> 1

