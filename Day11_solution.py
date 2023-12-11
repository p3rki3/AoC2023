import AoCFramework as AoC

def solve(expfactor):
    answer = 0
    for count in range(len(Galaxies)):
        for count2 in range(count + 1, len(Galaxies)):
            empties, (g1r, g1c), (g2r, g2c) = 0, Galaxies[count], Galaxies[count2]
            for row in Erows:
                if min(g1r, g2r) < row < max(g1r, g2r):
                    empties += 1
            for col in Ecols:
                if min(g1c, g2c) < col < max(g1c, g2c):
                    empties += 1
            answer +=  abs(g1r - g2r) + abs(g1c - g2c) + empties * expfactor
    return answer

def process_file():
    rows, cols = [], []
    for countr, line in enumerate(Galaxy):
        for countc, char in enumerate(line):
            if char == '#':
                Galaxies.append((countr, countc))
                rows.append(countr)
                cols.append(countc)
    for count in range(max(len(Galaxy), len(Galaxy[0]))):
        if count not in rows:
            Erows.append(count)
        if count not in cols:
            Ecols.append(count)

Galaxy, Erows, Ecols, Galaxies = AoC.Init("data/day11.txt")[0], [], [], []
process_file()
AoC.verify(9545480, 406725732046)
AoC.run(solve(1), solve(1000000-1))
