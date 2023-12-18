import AoCFramework as AoC

def solve(part=1):
    dirs, dirs_t = [(0, 1), (1, 0), (0, -1), (-1, 0)], ['R', 'D', 'L', 'U']
    perimeter, x, y, coords = 0, 0, 0, [(0, 0)]
    for line in Lines:   #R 3 (#63d832)
        line2 = line.split(' ') if part == 1 else line.split('#')[1].split(')')[0]
        dirn = dirs[dirs_t.index(line2[0])] if part == 1 else dirs[int(line2[-1])]
        dist = int(line2[1]) if part == 1 else int(line2[:-1], 16)
        x, y, perimeter = x + dirn[0] * dist, y + dirn[1] * dist, perimeter + dist
        coords.insert(0, (x, y))
    return (sum((coords[pt][1] + coords[pt + 1][1]) * (coords[pt][0] - coords[pt + 1][0]) for pt in range(len(coords) - 1)) // 2 + perimeter // 2 + 1)

Lines = AoC.Init("data/day18.txt")[0]
AoC.verify(48400, 72811019847283)
AoC.run(solve(), solve(2))
