import AoCFramework as AoC
from math import prod

AoC.Init(None)
Puzzle1 = [(41, 244), (66, 1047), (72, 1228), (66, 1040)]
Puzzle2 = [(41667266, 244104712281040)]
AoC.verify(74698, 27563421)
AoC.run(prod((t - 2*int(t/2 - (t*t/4 - d)**.5) - 1) for (t, d) in Puzzle1), sum((t - 2*int(t/2 - (t*t/4 - d)**.5) - 1) for (t, d) in Puzzle2))
