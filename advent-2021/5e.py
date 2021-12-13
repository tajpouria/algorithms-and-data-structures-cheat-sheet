inp = []
mx = 0
my = 0
for l in open("5e.in").read().strip().split("\n"):
  prs = [p.strip() for p in l.split("->")]
  nps = []
  for p in prs:
    np = [int(po) for po in p.split(",")]
    nps.append(np)
 
  p1, p2 = nps
  x1, y1 = p1
  x2, y2 = p2

  mx = max(x1, x2, mx)
  my = max(y1, y2, my)

  inp.append(sorted(nps, key=lambda p: (p[0], p[1])))

mtx = [[0 for x in range(mx + 1)] for _ in range(my + 1)]

for prs in inp:
  print(prs)
  p1, p2 = prs 
  x1, y1 = p1
  x2, y2 = p2

  if x1 == x2:
    for y in range(y2 - y1 + 1):
      mtx[y1 + y][x1] += 1
  elif y1 == y2:
    for x in range(x2 - x1 + 1):
      mtx[y1][x1 + x] += 1
  elif x2 > x1 and y2 > y1:
    for i in range(x2 - x1 + 1):
      mtx[y1 + i][x1 + i] += 1
  elif x2 > x1 and y2 < y1:
    for i in range(x2 - x1 + 1):
      mtx[y1 - i][x1 + i] += 1

res = 0
for l in mtx:
  print(l)
  for p in l:
    if p >= 2:
      res += 1

print(res)

