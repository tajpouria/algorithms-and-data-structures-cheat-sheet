inp = [[l.split(" ")[0], int(l.split(" ")[1])] for l in open("./2e.in").read().strip().split("\n")]

sm = {"p": 0, "a": 0, "h": 0}

for c, v in inp:
    if c == "down":
        sm["a"] += v
    if c == "up":
        sm["a"] -= v
    if c == "forward":
        sm["p"] += v
        sm["h"] += sm["a"] * v

print(sm, sm["p"] * sm["h"])

