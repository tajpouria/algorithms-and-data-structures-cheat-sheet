from collections import defaultdict

inp = defaultdict(int)
for el in [int(el) for el in open("6e.in").read().strip().split(",")]:
    if el not in inp:
        for i in range(el + 1):
            if i not in inp:
                inp[i] = 0
    inp[el] += 1

for el in range(9):
    if el not in inp:
        inp[el] = 0

for d in range(256):
    z = inp[0]
    inp[0] = 0
    for i in range(1, len(inp)):
        inp[i - 1] += inp[i]
        inp[i] = 0
    inp[6] += z
    inp[8] += z

print(sum(inp.values()))

