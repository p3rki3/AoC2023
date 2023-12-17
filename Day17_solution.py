import AoCFramework as AoC
from heapq import heappop, heappush

def solve(part):
    queue1, deck1 = [(0, 0, 0, 0, 0)], {}
    while queue1:
        heatloss, row, col, dirn, steps = heappop(queue1)
        if (row, col, dirn, steps) in deck1:
            continue
        deck1[(row, col, dirn, steps)] = heatloss
        for count, (deltarow, deltacol) in enumerate([[1,0], [0,1], [-1,0], [0,-1]]):
            nextrow, nextcol, new_dirn = row + deltarow, col + deltacol, count
            new_steps = (1 if new_dirn != dirn else steps + 1)
            constraint = (new_steps <= 3) if part == 1 else (new_steps <= 10 and (heatloss == 0 or new_dirn == dirn or steps >= 4))
            no_turning_back = ((new_dirn + 2) % 4 != dirn)
            if 0 <= nextrow < Rows and 0 <= nextcol < Cols and no_turning_back and constraint:
                heappush(queue1, (heatloss + Grid[nextrow][nextcol], nextrow, nextcol, new_dirn, new_steps))
    return min(set(heatloss for (row, col, _, _), heatloss in deck1.items() if row == Rows - 1 and col == Cols - 1))

Grid = [[int(num) for num in line] for line in AoC.Init("data/day17.txt", test=False)[0]]
Rows, Cols = len(Grid), len(Grid[0])
AoC.verify(1244, 1367)
AoC.run(solve(1), solve(2))
