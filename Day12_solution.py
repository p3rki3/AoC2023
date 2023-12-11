import AoCFramework as AoC

def part_1():
    p1answer = 0
    return p1answer


def part_2():
    p2answer = 0
    return p2answer

   
def process_file():
    global Lines
    for line in Lines:
        line = line


Lines, numlines = AoC.Init("data/day11.txt", nolines=False, isnumlist=False, printme=False)
process_file()
AoC.verify(None, None)
AoC.run(part_1, part_2)
