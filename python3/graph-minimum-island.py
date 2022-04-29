# https://structy.net/problems/minimum-island

def explore(g, ri, ci, vi):
    if not 0 <= ri < len(g): return 0
    if not 0 <= ci < len(g[ri]): return 0

    if g[ri][ci] == 'W': return 0

    l = f"{ri},{ci}"
    if vi.get(l): return 0
    vi[l] = 1
    
    s = sum(
            [ 
                1,
                explore(g, ri + 1, ci, vi),
                explore(g, ri - 1, ci, vi),
                explore(g, ri, ci + 1, vi),
                explore(g, ri, ci - 1, vi),
            ]
        )

    return s


def minimum_island(g):
    res = 0
    vi = {}

    for ri in range(len(g)):
        for ci in range(len(g)):
            s = explore(g, ri, ci, vi)
            if res == 0: res = s
            if s > 0:
                res = min(res, s)

    return res


grid = [
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'W', 'W', 'L', 'W'],
  ['W', 'W', 'L', 'L', 'W'],
  ['L', 'W', 'W', 'L', 'L'],
  ['L', 'L', 'W', 'W', 'W'],
]

print(minimum_island(grid)) # -> 2

grid = [
  ['L', 'W', 'W', 'L', 'W'],
  ['L', 'W', 'W', 'L', 'L'],
  ['W', 'L', 'W', 'L', 'W'],
  ['W', 'W', 'W', 'W', 'W'],
  ['W', 'W', 'L', 'L', 'L'],
]

print(minimum_island(grid)) # -> 1

grid = [
  ['L', 'L', 'L'],
  ['L', 'L', 'L'],
  ['L', 'L', 'L'],
]

print(minimum_island(grid))# -> 9

grid = [
  ['W', 'W'],
  ['L', 'L'],
  ['W', 'W'],
  ['W', 'L']
]

print(minimum_island(grid)) # -> 1

