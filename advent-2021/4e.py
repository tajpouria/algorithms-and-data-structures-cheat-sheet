import sys

infile = sys.argv[1] if len(sys.argv) > 1 else "4e.in"

# parse input
numbers = None
B = []
F = []
board = []
for line in open(infile):
    line = line.strip()
    if numbers is None:
        numbers = [int(x) for x in line.split(",")]
    else:
        if line:
            board.append([int(x) for x in line.split()])
        else:
            if board:
                B.append(board)
            board = []
B.append(board)

for b in B:
    assert len(b) == 5 and len(b[0]) == 5
    F.append([[False for _ in range(5)] for _ in range(5)])

WON = [False for _ in range(len(B))]
for num in numbers:
    for i in range(len(B)):
        for r in range(5):
            for c in range(5):
                if B[i][r][c] == num:
                    F[i][r][c] = True

        won = False
        for r in range(5):
            ok = True
            for c in range(5):
                if not F[i][r][c]:
                    ok = False
            if ok:
                won = True
        for c in range(5):
            ok = True
            for r in range(5):
                if not F[i][r][c]:
                    ok = False
            if ok:
                won = True
        if won and not WON[i]:
            WON[i] = True
            nwin = len([j for j in range(len(B)) if WON[j]])
            if nwin == 1 or nwin == len(B):
                unmarked = 0
                for r in range(5):
                    for c in range(5):
                        if not F[i][r][c]:
                            unmarked += B[i][r][c]
                print(unmarked * num)
