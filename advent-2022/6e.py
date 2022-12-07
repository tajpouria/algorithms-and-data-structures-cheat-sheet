fn = __file__.split(".")[0] + ".in"
txt = open(fn).read().strip()

s = []
for i in range(14):
    s.append(txt[i])

if list(set(s)) == s:
    print(14)
else:
    for i, el in enumerate(txt[14:]):
        s.pop(0)
        s.append(el)
        
        if len(set(s)) == 14:
            print(i+1+14)
            break
