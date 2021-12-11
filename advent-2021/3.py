inp = [l for l in open("3.in").read().strip().split("\n")]

g = ""
e = ""
for i in range(len(inp[0])):
    zc = 0
    oc = 0
    for l in inp:
        tar = l[i]
        if tar == "0":
            zc += 1
        else:
            oc += 1
    
    g += "0" if zc > oc else "1"
    e += "1" if zc > oc else "0"

print(int(g, 2)* int(e, 2))

