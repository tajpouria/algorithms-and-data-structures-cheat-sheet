inp = [ int(i) for i in open("1e.in").read().strip().split("\n") ]

win_size = 3

pws = 0
res = 0
for i in range(len(inp) - win_size + 1):
    w = inp[i:i+win_size]
    cws = sum(w)
    if i > 0 and cws > pws:
        res += 1 

    pws = cws

print(res)

