import AoCFramework as AoC
from collections import defaultdict
from math import prod

def part_1():
    p1answer, adj, Gears = 0, [1, 0, -1], set()
    for row in range(rows):
        num, is_part = 0, False
        for col in range(cols + 1):
            if col < cols and Board[row][col].isdigit():
                num = num * 10 + int(Board[row][col])
                for drow in adj:
                    for dcol in adj:
                        if 0 <= row + drow < rows and 0 <= col + dcol < cols:
                            ch = Board[row + drow][col + dcol]
                            if ch != '.' and not ch.isdigit():
                                is_part = True
                            if ch == '*':
                                Gears.add((row + drow, col + dcol))
            elif num > 0:
                p1answer += num if is_part else 0
                for gear in Gears:
                    Nums[gear].append(num)
                num, Gears, is_part = 0, set(), False
    return p1answer
   
def part_2():
    return sum(prod(n) for n in Nums.values() if len(n) == 2)
   
Board, rows = AoC.Init("data/day3.txt")
cols, Nums = len(Board[0]), defaultdict(list)
AoC.verify(532331, 82301120)
AoC.run(part_1, part_2)
