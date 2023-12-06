import AoCFramework as AoC

def part_1(puzzle):
    answer = 1
    for (t, d) in puzzle:
        raceswon = 0
        for i in range(t):
            if(i * (t-i) > d):
                raceswon += 1
        answer *= raceswon
    return answer

AoC.Init(None)
Puzzle1 = [(41, 244), (66, 1047), (72, 1228), (66, 1040)]
Puzzle2 = [(41667266, 244104712281040)]
AoC.verify(74698, 27563421)
AoC.run(part_1(Puzzle1), part_1(Puzzle2))
