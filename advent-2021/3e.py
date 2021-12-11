inp = [l for l in open("3e.in").read().strip().split("\n")]


ox = inp.copy()

for i in range(len(inp[0])):
    zc = 0
    oc = 0
    for l in ox:
        tar = l[i]
        if tar == "0":
            zc += 1
        else:
            oc += 1

    nox = []
    for l in ox:
        tar = l[i]

        if zc > oc:
            if tar == "0":
                nox.append(l)
        else:
            if tar == "1":
                nox.append(l)
    ox = nox



cx = inp.copy()

for i in range(len(inp[0])):
    zc = 0
    oc = 0
    for l in cx:
        tar = l[i]
        if tar == "0":
            zc += 1
        else:
            oc += 1

    ncx = []
    for l in cx:
        tar = l[i]

        if oc < zc:
            if tar == "1":
                ncx.append(l)
        else:
            if tar == "0":
                ncx.append(l)
    cx = ncx

    if len(cx) == 1:
        break


print(int(ox[0], 2) * int(cx[0], 2))

