import AoCFramework as AoC
from z3 import Int, Solver, sat

def part_1():
    p1answer, lower, upper = 0, 2*10**14, 4*10**14
    for s1 in range(stones):
        x1, x2, y1, y2 = Stones[s1][0], Stones[s1][0] + Stones[s1][3], Stones[s1][1], Stones[s1][1] + Stones[s1][4]
        for s2 in range(s1 + 1, stones):
            x3, x4, y3, y4 = Stones[s2][0], Stones[s2][0] + Stones[s2][3], Stones[s2][1], Stones[s2][1] + Stones[s2][4]
            try:
                divisor, factor1, factor2 = ((x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)), (x1 * y2 - y1 * x2), (x3 * y4 - y3 * x4)
                interpolx, interpoly = (factor1 * (x3 - x4) - factor2 * (x1 - x2)) / divisor, (factor1 * (y3 - y4) - factor2 * (y1 - y2)) / divisor
                isfuture = ((interpolx > x1) == (x2 > x1)) and ((interpolx > x3) == (x4 > x3))
                p1answer += 1 if lower <= interpolx <= upper and lower <= interpoly <= upper and isfuture else 0
            except:  pass # divide by zero for parallel trajectories
    return p1answer

def part_2():
    posx, posy, posz, velx, vely, velz = Int('posx'), Int('posy'), Int('posz'), Int('velx'), Int('vely'), Int('velz')
    Solve, Time = Solver(), [Int(f'T{i}') for i in range(stones)]
    for stone in range(stones):
        Solve.add(posx + Time[stone] * velx - Stones[stone][0] - Time[stone] * Stones[stone][3] == 0)
        Solve.add(posy + Time[stone] * vely - Stones[stone][1] - Time[stone] * Stones[stone][4] == 0)
        Solve.add(posz + Time[stone] * velz - Stones[stone][2] - Time[stone] * Stones[stone][5] == 0)
    return Solve.model().eval(posx + posy + posz) if str(Solve.check()) == 'sat' else 'Failed to solve constraints'

Stones, Lines, stones = [], *AoC.Init("data/day24.txt", test=False)
for line in Lines:
    Stones.append([int(p) for p in line.replace(' @', ',').split(', ')])
AoC.verify(24627, 527310134398221)
AoC.run(part_1, part_2)
