inf = __file__.split(".")[0] + ".in"
elfs = open(inf).read().strip().split("\n\n")
ls = []
for el in elfs:
    arr = [int(c) for c in el.split("\n")]
    ls.append(sum(arr))

ls.sort()
print(ls)
print(sum(ls[-3:]))

