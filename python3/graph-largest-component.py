from collections import deque

def largest_component(g):
    vi = {}
    res = 0
    for n in g:
        if vi.get(n): continue
        q = deque([n])
        cres = 0 
        while(len(q)):
            c = q.popleft()
            vi[c] = True
            for ne in g.get(c):
                if not vi.get(ne):
                    q.append(ne)
                    cres += 1
            
        res = max(res, cres)

    return res

print(
    largest_component({
        0: [8, 1, 5],
        1: [0],
        5: [0, 8],
        8: [0, 5],
        2: [3, 4],
        3: [2, 4],
        4: [3, 2]
    })
) # -> 4
