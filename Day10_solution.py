import AoCFramework as AoC

def pipe(c, i, j):
    match c:
        case '|': return (i-1,j), (i+1,j)
        case '-': return (i,j-1), (i,j+1)
        case 'L': return (i-1,j), (i,j+1)
        case 'J': return (i-1,j), (i,j-1)
        case '7': return (i+1,j), (i,j-1)
        case 'F': return (i+1,j), (i,j+1)

def connected_to(pt):
    return set(pipe(Pipes[*pt], *pt))

def part_1():
    global Visited
    endpt1, endpt2 = [pt for di,dj in ((-1,0),(0,1),(0,-1),(1,0)) if (pt:=(Start[0]+di,Start[1]+dj)) in Pipes and Start in connected_to(pt)]
    for c in '|-LJ7F':
        if set(pipe(c, *Start)) == set([endpt1, endpt2]):
            Pipes[Start] = c
    Visited, steps = set([Start, endpt1, endpt2]), 1
    while endpt1 != endpt2:
        endpt1, endpt2 = (connected_to(endpt1) - Visited).pop(), (connected_to(endpt2) - Visited).pop()
        Visited |= set([endpt1, endpt2])
        steps += 1
    return steps

def part_2():
    enclosed = 0
    for i in range(len(Lines)):
        inside = False
        for j in range(len(Lines[0])):
            if (i,j) in Visited:
                if Pipes[i,j] in '|LJ':
                    inside = not inside
                continue
            if inside: enclosed += 1
    return enclosed
   
def process_file():
    global Pipes, Start
    Pipes = dict()
    for i, line in enumerate(Lines):
        for j, ch in enumerate(line):
            if ch == 'S': Start = (i,j)
            elif ch != '.': Pipes[i,j] = ch

Pipes, Start, Visited, Lines = None, None, None, AoC.Init("data/day10.txt")[0]
process_file()
AoC.verify(6856, 501)
AoC.run(part_1, part_2)