# read the input from a file called 8.in
txt = open(__file__.split(".")[0] + ".in").read()

# txt = """30373
# 25512
# 65332
# 33549
# 35390"""

# Turn txt into a grid of integers
g = [[int(c) for c in ln] for ln in txt.strip().split("\n")]

# A visible item in a grid is a item
# if all the items between it and the edge of the grid
# are smaller than it
def vis(g, x, y):
    # return True if the item is on the edge of the grid
    if x == 0 or y == 0 or x == len(g[y]) - 1 or y == len(g) - 1:
        return True

    # Check up
    for y2 in range(y):
        if g[y2][x] >= g[y][x]:
            break
    else:
        return True

    # Check down
    for y2 in range(y + 1, len(g)):
        if g[y2][x] >= g[y][x]:
            break
    else:
        return True

    # Check left
    for x2 in range(x):
        if g[y][x2] >= g[y][x]:
            break
    else:
        return True

    # Check right
    for x2 in range(x + 1, len(g[y])):
        if g[y][x2] >= g[y][x]:
            break
    else:
        return True

    return False


# Count the number of visible items in a grid
def count_vis(g):
    c = 0
    for y in range(len(g)):
        for x in range(len(g[y])):
            if vis(g, x, y):
                print(f"Visiable: {g[y][x]} ({x}, {y})")
                c += 1
    return c


print(count_vis(g))
