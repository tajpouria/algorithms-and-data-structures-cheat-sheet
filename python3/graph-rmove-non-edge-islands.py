# https://www.youtube.com/watch?v=4tYoVx0QoN0

def explore(g, ri, ci, vi):
    if not 0 <= ri < len(g): return []
    if not 0 <= ci < len(g[ri]): return []

    if g[ri][ci] != 1: return []

    p= f"{ri},{ci}"
    if vi.get(p): return []
    vi[p] = 1

    prc = [ri, ci]

    prc += explore(g, ri + 1, ci, vi)
    prc += explore(g, ri - 1, ci, vi)
    prc += explore(g, ri, ci + 1, vi)
    prc += explore(g, ri, ci - 1, vi)

    return prc


def remove_islands(g):
    vi = {}
    iss = []
    for ri in range(len(g)):
        for ci in range(len(g[ri])):
            res = explore(g, ri, ci, vi)
            if res: iss.append(res)

    # [[0, 0], [1, 1], [1, 3, 1, 4, 2, 4, 3, 4, 1, 5], [2, 2], [3, 0, 4, 0, 5, 0, 3, 1], [4, 2, 4, 3], [5, 5]]
    tbr = []
    for i in iss:
        ind = True
        for j in range(len(i)):
            if (j % 2) == 0:
                if i[j] == 0 or i[j] == (len(g) - 1): 
                    ind = False
                    break
            else:
                if i[j] == 0 or i[j] == (len(g[0]) - 1):
                    ind = False
                    break
        if ind: tbr.append(i)

    # [[1, 1], [2, 2], [4, 2, 4, 3]] for i in tbr:
    for i in tbr: 
        for j in range(len(i)):
            if (j % 2) == 0:
                ri = i[j]
                ci = i[j+1]
                g[ri][ci] = 0


matrix = [
    [1, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 1, 1],
    [0, 0, 1, 0, 1, 0],
    [1, 1, 0, 0, 1, 0],
    [1, 0, 1, 1, 0, 0],
    [1, 0, 0, 0, 0, 1],
]

remove_islands(matrix)
print(matrix)

# [
#     [1, 0, 0, 0, 0, 0],
#     [0, 0, 0, 1, 1, 1],
#     [0, 0, 0, 0, 1, 0],
#     [1, 1, 0, 0, 1, 0],
#     [1, 0, 0, 0, 0, 0],
#     [1, 0, 0, 0, 0, 1],
# ]

