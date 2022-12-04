import string

fn = __file__.split(".")[0] + ".in"
txt = open(fn).read()

lc = {}
for i, a in enumerate(list(string.ascii_lowercase)):
    lc[a] = i + 1

uc = {}
for i, a in enumerate(list(string.ascii_uppercase)):
    uc[a] = i + 1 + 26

ts = 0

for rc in txt.strip().split("\n"):
    fh, sh = rc[:len(rc)//2], rc[len(rc)//2:]

    cel = ""
    for el in fh:
        if sh.find(el) > -1:
            cel = el
            break


    ts += lc[cel] if cel.islower() else uc[cel]

print(ts)

