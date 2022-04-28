# https://structy.net/problems/connected-components-count
from collections import deque

def connected_components_count(g):
    vi = {}
    res = 0
    for n in g.keys():
        if vi.get(n): continue
        res += 1
        s = deque([n])
        while(len(s)):
           c = s.pop() 
           vi[c] = True
           for ne in g.get(c): 
               if not vi.get(ne): s.append(ne)
       
    return res


print(
    connected_components_count({
      0: [8, 1, 5],
      1: [0],
      5: [0, 8],
      8: [0, 5],
      2: [3, 4],
      3: [2, 4],
      4: [3, 2]
    }) # -> 2
)
