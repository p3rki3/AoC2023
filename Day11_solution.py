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
    for count, line in enumerate(Galaxy):
        if line.find('#') == -1:
            Erows.append(count)
    for count in range(len(Galaxy[0])):
        empty = True
        for line in Galaxy:
            if line[count] =='#':
                empty = False
        if empty is True:
            Ecols.append(count)
    for countr, line in enumerate(Galaxy):
        for countc, char in enumerate(line):
            if char == '#':
                Galaxies.append((countr, countc))

Galaxy, Erows, Ecols, Galaxies = AoC.Init("data/day11.txt")[0], [], [], []
process_file()
AoC.verify(9545480, 406725732046)
AoC.run(solve(1), solve(1000000-1))
