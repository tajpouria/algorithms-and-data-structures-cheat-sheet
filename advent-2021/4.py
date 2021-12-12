txt = open("4.in").read().split("\n")

mrks = [int(n) for n in txt[0].split(",")]

brds = []

rc = []
for l in txt[2:]:
    if l == "":
        brds.append(rc)
        rc = []
        continue

    r = [int(n) for n in l.strip().split()]
    rc.append(r)


wb = []
wel = 0
for el in mrks:
    for bi, b in enumerate(brds):
        for bli, bl in enumerate(b):
            if el in bl:
                bl.remove(el)
            
            if len(bl) == 0:
                wb = b
                wel = el
                break
        else:
            continue
        break
    else:
        continue
    break

s=0
for bl in wb:
    s += sum(bl)

print(s*wel)

