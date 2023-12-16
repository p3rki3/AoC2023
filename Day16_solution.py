import AoCFramework as AoC

def part_1(initr=0,initc=0,initdirn=1):
    posn, seen = [(initr, initc, initdirn)], set()
    nextblock = lambda row, col, dirn: (row + [-1,0,1,0][dirn], col + [0,1,0,-1][dirn], dirn)
    while True:
        if len(posn) == 0:
            break
        nextpos = []
        for (row, col, dirn) in posn:
            if 0 <= row < Rows and 0 <= col < Cols:
                if (row, col, dirn) in seen:
                    continue
                seen.add((row, col, dirn))
                match Grid[row][col]:
                    case '.':
                        nextpos.append(nextblock(row, col, dirn))
                    case '/':
                        nextpos.append(nextblock(row, col, {0:1, 1:0, 2:3, 3:2}[dirn]))
                    case '\\':
                        nextpos.append(nextblock(row, col, {0:3, 1:2, 2:1, 3:0}[dirn]))
                    case '|':
                        if dirn % 2 == 1:
                            nextpos.append(nextblock(row, col, 0))
                            nextpos.append(nextblock(row, col, 2))
                        else:
                            nextpos.append(nextblock(row, col, dirn))
                    case '-':
                        if dirn % 2 == 0:
                            nextpos.append(nextblock(row, col, 1))
                            nextpos.append(nextblock(row, col, 3))
                        else:
                            nextpos.append(nextblock(row, col, dirn))
        posn = nextpos
    return len(set((row, col) for (row, col, _) in seen))

def part_2():
    p2answer = []
    for row in range(Rows):
        p2answer.append(part_1(row, 0, 1))
        p2answer.append(part_1(row, Cols - 1, 3))
    for col in range(Cols):
        p2answer.append(part_1(0, col, 2))
        p2answer.append(part_1(Rows - 1, col, 0))
    return max(p2answer)

Grid = [[char for char in lines] for lines in AoC.Init("data/day16.txt", test=False)[0]]
Rows, Cols = len(Grid), len(Grid[0])
AoC.verify(7927, 8246)
AoC.run(part_1, part_2)
