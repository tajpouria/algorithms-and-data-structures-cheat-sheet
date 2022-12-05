import re

fn = __file__.split(".")[0] + ".in"
txt = open(fn).read()

st, ins = txt.split("\n\n")

cbi = st.find("1")
cei = len(st) - 1

xis = []
for i, el in enumerate(txt[cbi-1:cei+1]):
    if el != " ":
        xis.append(i)

di = {}
for x in xis:
    di[x] = []

for l in txt[:cbi-2].split("\n"):
    for i, el in enumerate(l):
        if el not in [" ", "[", "]", "\n"]:
            di[i].append(el)

mtx = list(di.values())

for l in ins.strip().split("\n"):
    c, si, di = [int(e) for e in re.sub(r"(move )|(from )|( to)", "", l).split(" ")]

    for _ in range(c):
        el = mtx[si-1].pop(0)
        mtx[di-1].insert(0, el) 

res = ""
for s in mtx:
    res += s[0]

print(res)

