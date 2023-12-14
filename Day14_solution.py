import AoCFramework as AoC

def load():
    answer = 0
    for r, row in enumerate(Grid):
        countO = ''.join(row).count('O')
        answer += countO * (rows - r)
    return answer

def north():
    for r in range(1, rows):
        for c in range(cols):
            if Grid[r][c] == 'O' and Grid[r-1][c] == '.':
                rr = r - 1
                while rr > 0 and Grid[rr-1][c] == '.':
                    rr -= 1
                Grid[rr][c], Grid[r][c] = 'O', '.'

def wse():
    for c in range(1, cols):
        for r in range(rows):
            if Grid[r][c] == 'O' and Grid[r][c-1] == '.':
                cc = c - 1
                while cc > 0 and Grid[r][cc-1] == '.':
                    cc -= 1
                Grid[r][cc], Grid[r][c] = 'O', '.'
    for r in range(rows-2, -1, -1):
        for c in range(cols):
            if Grid[r][c] == 'O' and Grid[r+1][c] == '.':
                rr = r + 1
                while rr < rows -1 and Grid[rr+1][c] == '.':
                    rr += 1
                Grid[rr][c], Grid[r][c] = 'O', '.'
    for c in range(cols-2, -1, -1):
        for r in range(rows):
            if Grid[r][c] == 'O' and Grid[r][c+1] == '.':
                cc = c + 1
                while cc < cols -1 and Grid[r][cc+1] == '.':
                    cc += 1
                Grid[r][cc], Grid[r][c] = 'O', '.'

def part_1():
    north()
    return load()

def part_2():
    cycles, cache = 1, {}
    wse()
    while cycles < spincycles:
        north()
        wse()
        cycles += 1
        Grid2 = tuple(tuple(row) for row in Grid)
        if Grid2 in cache:
            cycle_len = cycles - cache[Grid2]
            cycles += ((spincycles - cycles) // cycle_len) * cycle_len
            cache = {}
        else:
            cache[Grid2] = cycles
    return load()

Grid = [[ch for ch in line] for line in AoC.Init("data/day14.txt")[0]]
rows, cols, spincycles = len(Grid), len(Grid[0]), 10**9
AoC.verify(105784, 91286)
AoC.run(part_1, part_2)
