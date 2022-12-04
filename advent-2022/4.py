fn = __file__.split(".")[0] + ".in"
txt = open(fn).read()

ts = 0
for ro in txt.strip().split("\n"):
    fc, sc = ro.split(",")

    fa, fb = [int(n) for n in fc.split("-")]
    sa, sb = [int(n) for n in sc.split("-")]

    if (fa <= sa and fb >= sb) or (sa <= fa and sb >= fb):
        ts += 1

print(ts)
