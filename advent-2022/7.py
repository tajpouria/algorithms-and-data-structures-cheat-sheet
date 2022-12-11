txt = open(__file__.split(".")[0] + ".in").read()

# txt = """$ cd /
# $ ls
# dir a
# 14848514 b.txt
# 8504156 c.dat
# dir d
# $ cd a
# $ ls
# dir e
# 29116 f
# 2557 g
# 62596 h.lst
# $ cd e
# $ ls
# 584 i
# $ cd ..
# $ cd ..
# $ cd d
# $ ls
# 4060174 j
# 8033020 d.log
# 5626152 d.ext
# 7214296 k"""

t = {}
c = []
for ln in txt.strip().split("\n")[1:]:
    if ln == "$ ls":
        continue

    if ln.startswith("$"):
        _, cmd, arg = ln.split(" ")
        if cmd == "cd":
            if arg == "..":
                c.pop()
            else:
                c.append(arg)
    else:
        ld = t
        for d in c:
            ld = ld[d]

        if ln.startswith("dir"):
            _, dn = ln.split(" ")
            ld[dn] = {}
        else:
            fs, fn = ln.split(" ")
            ld[fn] = int(fs)


print(t)


def ds(t=t, rt={}, ck="/"):
    s, sds = 0, 0
    for itk, it in t.items():
        if isinstance(it, dict):
            sep = "/" if ck != "/" else ""
            sds, _ = ds(it, rt, ck + sep + itk)
        else:
            s += it
    rt[ck] = s + sds
    return rt[ck], rt


_, rt = ds()

print((sum(filter(lambda d: d <= 100000, rt.values()))))
