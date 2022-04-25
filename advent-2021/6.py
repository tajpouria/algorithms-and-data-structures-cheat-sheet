inp = [int(el) for el in open("6.in").read().strip().split(",")]

for d in range(1, 267):
    for i in range(len(inp)):
        inp[i] -= 1

        if inp[i] == -1:
            inp.append(8)
            inp[i] += 7
            continue


    print(f"day {d}: ", inp)

print(len(inp))

