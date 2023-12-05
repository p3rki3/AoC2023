import AoCFramework as AoC

def part_1():
    p1answer, res = [], 0
    for seed in Seeds:
        res = seed
        for transl in range(7):
            for val in TransTabs[transl]:
                if val[1] <= res < val[1] + val[2]:
                    res += (val[0] - val[1])
                    break
        p1answer.append(res)
    return min(p1answer)


def part_2():
    p2answer = []
    for i in range(0, len(Seeds), 2):
        seedstart, seedrange, skip = Seeds[i], Seeds[i+1], Seeds[i+1]
        nextseed = seedstart
        while nextseed <= seedstart + seedrange:
            res = nextseed
            for transl in range(7):
                for val in TransTabs[transl]:
                    if val[1] <= res < val[1] + val[2]:
                        skip = min(skip, val[1] + val[2] - res)
                        res += (val[0] - val[1])
                        if skip <= 0:
                            skip = 1
                        break
            p2answer.append(res)
            nextseed += skip
            skip = seedrange - nextseed + seedstart
    return min(p2answer)

def process_file():
    global Seeds, Transtabs
    proctype = -1
    for line in Lines:
        if len(line) < 3:
            pass
        elif line[0:5] == 'seeds':
            Seeds = [int(n) for n in line[7:].split(' ')]
        elif ':' in line:
            proctype += 1
        else:
            numlist = [int(n) for n in line.split(' ')]
            TransTabs[proctype].append(numlist)
   
Seeds, TransTabs = [], [[],[],[],[],[],[],[]]
Lines = AoC.Init("data/Day5.txt")[0]
process_file()
AoC.verify(111627841, 69323688)
AoC.run(part_1, part_2)
