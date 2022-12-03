inf = __file__.split(".")[0] + ".in" 
txt = open(inf).read().strip()

scores = {"X": 1, "Y": 2, "Z": 3}

sc = 0

for h in txt.split("\n"):
    m, u = h.split()

    if m == "A": # Rock
        if u == "X": # Rock
            sc += scores[u] + 3
        elif u == "Y": # Paper
            sc += scores[u] + 6
        elif u == "Z": # Scissors
            sc += scores[u] + 0
    elif m == "B": # Paper
        if u == "X": # Rock
            sc += scores[u] + 0
        elif u == "Y": # Paper
            sc += scores[u] + 3
        elif u == "Z": # Scissors
            sc += scores[u] + 6
    elif m == "C": # Scissors
        if u == "X": # Rock
            sc += scores[u] + 6
        elif u == "Y": # Paper
            sc += scores[u] + 0
        elif u == "Z": # Scissors
            sc += scores[u] + 3
print(sc)
