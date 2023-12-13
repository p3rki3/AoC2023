import AoCFramework as AoC

def solve():
    answer1 = answer2 = 0
    for grid in Grids:
        grid = [[char for char in line] for line in grid.split('\n')]
        rows, cols = len(grid), len(grid[0])
        for row in range(rows - 1):
            errors = 0
            for row2 in range(rows - row - 1):
                up, down = row - row2, row + row2 + 1
                if 0 <= up < down < rows:
                    for col in range(cols):
                        if grid[up][col] != grid[down][col]:
                            errors += 1
            answer1 += (row + 1) * 100 * (errors == 0)
            answer2 += (row + 1) * 100 * (errors == 1)
        for col in range(cols - 1):
            errors = 0
            for col2 in range(cols - col - 1):
                left, right = col - col2, col + col2 + 1
                if 0 <= left < right < cols:
                    for row in range(rows):
                        if grid[row][left] != grid[row][right]:
                            errors += 1
            answer1 += (col + 1) * (errors == 0)
            answer2 += (col + 1) * (errors == 1)
    return (answer1, answer2)

Grids = AoC.Init("data/day13.txt", nolines=True).split('\n\n')
AoC.verify(37561, 31108)
AoC.run(solve)
