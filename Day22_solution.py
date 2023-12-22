import AoCFramework as AoC
from copy import deepcopy

def solve():
    global Bricks
    p1answer, p2answer, goaround = 0, 0, True
    occupied = set((x, y, z) for brick in Bricks for (x, y, z) in brick)
    while goaround: # Now drop the bricks in the air
        goaround = False
        for count, brick in enumerate(Bricks):
            candrop = True
            for (x, y, z) in brick:
                candrop = False if z == 1 or ((x, y, z-1) in occupied and (x, y, z-1) not in brick) else candrop
            if candrop:
                goaround = True
                for (x, y, z) in brick:
                    occupied.discard((x, y, z))
                    occupied.add((x, y, z - 1))
                Bricks[count] = [(x, y, z - 1) for (x, y, z) in brick]
    for count, brick in enumerate(Bricks):
        cpoccupied, cpBricks = deepcopy(occupied), deepcopy(Bricks)
        for (x, y, z) in brick:
            cpoccupied.discard((x, y, z))
        goaround, canfall = True, set()
        while goaround:
            goaround = False
            for count2, brick2 in enumerate(cpBricks):
                if count == count2:
                    continue
                candrop = True
                for (x, y, z) in brick2:
                    candrop = False if z == 1 or ((x, y, z - 1) in cpoccupied and (x, y, z - 1) not in brick2) else candrop
                if candrop:
                    canfall.add(count2)
                    for (x, y, z) in brick2:
                        cpoccupied.discard((x, y, z))
                        cpoccupied.add((x, y, z - 1))
                    cpBricks[count2] = [(x, y, z - 1) for (x, y, z) in brick2]
                    goaround = True
        p1answer += 1 if len(canfall) == 0 else 0
        p2answer += len(canfall)
    return p1answer, p2answer

Bricks = []
for line in AoC.Init("data/day22.txt", test=False)[0]:
    sx, sy, sz = [int(num) for num in line.split('~')[0].split(',')]
    ex, ey, ez = [int(num) for num in line.split('~')[1].split(',')]
    Bricks.append([(x, sy, sz) for x in range(sx, ex + 1)] if sx != ex else [(sx, y, sz) for y in range(sy, ey + 1)] if sy != ey else [(sx, sy, z) for z in range(sz, ez + 1)])
AoC.verify(497, 67468)
AoC.run(solve)
