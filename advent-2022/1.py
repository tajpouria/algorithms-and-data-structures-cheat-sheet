inf = __file__.split(".")[0] + ".in"
elfs = open(inf).read().strip().split("\n\n")
m = 0
for el in elfs:
    arr = [ int(c) for c in el.split("\n") ]
    els = sum(arr)
    if els > m:
        m = els
print(m)

