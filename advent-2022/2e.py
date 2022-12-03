inf = __file__.split(".")[0] + ".in" 
txt = open(inf).read().strip()

scores = {"X": 1, "Y": 2, "Z": 3}
l = {"A": "Z", "B": "X", "C": "Y"} 
d = {"A": "X", "B": "Y", "C": "Z"} 
w = {"A": "Y", "B": "Z", "C": "X"} 

sc = 0

for h in txt.split("\n"):
    m, u = h.split()

    if m == "A": # Rock
        if u == "X": # Lose
            sc += scores[l[m]] + 0
        elif u == "Y": # Draw
            sc += scores[d[m]] + 3
        elif u == "Z": # Win
            sc += scores[w[m]] + 6
    elif m == "B": # Paper
        if u == "X": # Lose
            sc += scores[l[m]] + 0
        elif u == "Y": # Draw
            sc += scores[d[m]] + 3
        elif u == "Z": # Win
            sc += scores[w[m]] + 6
    elif m == "C": # Scissors
        if u == "X": # Lose
            sc += scores[l[m]] + 0
        elif u == "Y": # Draw
            sc += scores[d[m]] + 3
        elif u == "Z": # Win
            sc += scores[w[m]] + 6
print(sc)
