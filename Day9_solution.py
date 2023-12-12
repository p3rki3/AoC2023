import AoCFramework as AoC

def get_next(numline):
    diffs, lastnos = numline, [numline[-1]]
    while sum(abs(df) for df in diffs) > 0:
        diffs = [diffs[i+1] - diffs[i] for i in range(len(diffs) - 1)]
        lastnos.append(diffs[-1])
    return sum(lastnos)

AoC.verify(1584748274, 1026)
Nums = [[int(n) for n in line.split()] for line in AoC.Init("data/day9.txt")[0]]
AoC.run(sum(get_next(numline) for numline in Nums), sum(get_next(list(reversed(numline))) for numline in Nums))
