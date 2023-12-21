import AoCFramework as AoC
from collections import deque

def solve():
    Factors, nextfactor, p1answer, p2answer, goalsteps, Pos, dirs, target = [0, 0, 0], 0, 0, 0, 26501365, {Startpos}, [(1, 0),(0, 1), (-1, 0) ,(0, -1)], Rows // 2
    for count in range(1, 1000):
        npos = set()
        for r, c in Pos:
            for dirn in dirs:
                nr, nc = r + dirn[0], c + dirn[1]
                if Grid[nr % Rows][nc % Cols] != "#":
                    npos.add((nr, nc))
        Pos = npos
        if count == target + Rows * nextfactor:
            Factors[nextfactor] = len(Pos)
            nextfactor += 1
            if nextfactor == 3:
                delta0, delta1, delta2 = Factors[0], Factors[1] - Factors[0], Factors[2] - 2 * Factors[1] + Factors[0]
                p2answer = delta0 + delta1 * (goalsteps // Rows) + delta2 * ((goalsteps // Rows) * ((goalsteps // Rows) - 1) // 2)
                return p1answer, p2answer
        elif count == 64:
            p1answer = len(Pos)

Lines = AoC.Init("data/day21.txt", test=False)[0]
Grid = [[char for char in line] for line in Lines]
Rows, Cols, Startpos = len(Grid), len(Grid[0]), (0, 0)
for row in range(Rows):
    col = Lines[row].rfind('S')
    if col > -1:
        Startpos = (row, col)
        Grid[row][col] = '.'
AoC.verify(3776, 625587097150084)
AoC.run(solve)
