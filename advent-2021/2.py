inp = [ [ l.split(" ")[0], int(l.split(" ")[1]) ] for l in open("./2.in").read().strip().split("\n") ]


pos = {"h": 0, "d": 0}

for c, u in inp:
    if c == "forward":
        pos["h"] += u
    elif c == "down": 
        pos["d"] += u
    elif c == "up":
        pos["d"] -= u

print(pos["h"]*pos["d"])

