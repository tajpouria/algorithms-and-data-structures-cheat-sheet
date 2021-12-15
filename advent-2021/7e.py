import math

inp = [int(el) for el in open("7e.in").read().strip().split(",")] 

mx = max(inp)

def su(x):
    return x * (x - 1) // 2

min_res = math.inf
for p in range(mx + 1):
    total = 0
    for c in inp:
        total += su(abs(c - p) + 1)

    min_res = min(min_res, total)

print(min_res)

