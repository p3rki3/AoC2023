import AoCFramework as AoC

def solve(expfactor1, expfactor2):
    answer1 = answer2 = 0
    for count in range(len(Galaxies)):
        for count2 in range(count + 1, len(Galaxies)):
            empties, (g1r, g1c), (g2r, g2c) = 0, Galaxies[count], Galaxies[count2]
            (g1r, g2r) = (g1r, g2r) if g1r < g2r else (g2r, g1r)
            (g1c, g2c) = (g1c, g2c) if g1c < g2c else (g2c, g1c)
            for row in Erows:
                if g1r < row < g2r:
                    empties += 1
            for col in Ecols:
                if g1c < col < g2c:
                    empties += 1
            mhdist = g2r - g1r + g2c - g1c
            answer1 += mhdist + empties * expfactor1
            answer2 += mhdist + empties * expfactor2
    return answer1, answer2

def process_file():
    rows, cols = [], []
    for countr, line in enumerate(Galaxy):
        for countc, char in enumerate(line):
            if char == '#':
                Galaxies.append((countr, countc))
                rows.append(countr)
                cols.append(countc)
    for count in range(len(Galaxy)):
        if count not in rows:
            Erows.append(count)
    for count in range(len(Galaxy[0])):
        if count not in cols:
            Ecols.append(count)

Galaxy, Erows, Ecols, Galaxies = AoC.Init("data/day11.txt")[0], [], [], []
process_file()
AoC.verify(9545480, 406725732046)
AoC.run(solve(1, 1000000-1))
