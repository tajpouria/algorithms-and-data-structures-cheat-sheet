fn = __file__.split(".")[0] + ".in"
txt = open(fn).read().strip()

s = []
for i in range(4):
    s.append(txt[i])

if list(set(s)) == s:
    print(4)
else:
    for i, el in enumerate(txt[4:]):
        s.pop(0)
        s.append(el)
        
        if len(set(s)) == 4:
            print(i+1+4)
            break
