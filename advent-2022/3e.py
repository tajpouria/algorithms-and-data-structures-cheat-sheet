import string

fn = __file__.split(".")[0] + ".in"
txt = open(fn).read()

lc = {}
for i, a in enumerate(list(string.ascii_lowercase)):
    lc[a] = i + 1

uc = {}
for i, a in enumerate(list(string.ascii_uppercase)):
    uc[a] = i + 1 + 26

gs = []

inp = txt.strip().split("\n")
gs.append(zip(*list([iter(inp)]*3)))

ts = 0
for g in gs:
    for rs in g:
        fh, sh, th = rs

        cel = ""
        for el in fh:
            if sh.find(el) > -1 and th.find(el) > -1:
                cel = el
        
        ts += lc[cel] if cel.islower() else uc[cel]
        
print(ts)

