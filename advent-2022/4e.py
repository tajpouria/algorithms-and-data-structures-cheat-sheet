fn = __file__.split(".")[0] + ".in"
txt = open(fn).read()

ts = 0
for ro in txt.strip().split("\n"):
    fc, sc = ro.split(",")

    fa, fb = [int(n) for n in fc.split("-")]
    sa, sb = [int(n) for n in sc.split("-")]

    sr = list(range(sa, sb+1))
    for a in range(fa, fb+1):
        if a in sr:
            ts += 1
            break


print(ts)
