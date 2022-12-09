txt = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""

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
            fs, fn= ln.split(" ")
            ld[fn] = int(fs)


def find_directories(tree, max_size=100000, directories=[]):
    for key, value in tree.items():
        if isinstance(value, object):
            ts = sum(filter(lambda l: isinstance(l, int), value.values()))
            if ts <= max_size:
                directories.append((key, ts))

    return directories

directories = find_directories(t)

print(directories)
