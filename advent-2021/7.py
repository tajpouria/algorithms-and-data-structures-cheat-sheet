import math

inp = [int(el) for el in open("7.in").read().strip().split(",")] 

mx = max(inp)

min_res = math.inf
for p in range(mx + 1):
    total = 0
    for c in inp:
        total += abs(c - p)

    min_res = min(min_res, total)

print(min_res)

