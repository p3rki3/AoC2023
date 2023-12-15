import AoCFramework as AoC

def hashme(chars):
    eqhash = 0
    for char in chars:
        eqhash = ((eqhash + ord(char)) * 17) % 256
    return eqhash

def part_2():
    p2answer, lensbox = 0, [[] for _ in range(256)]
    for eq in Equations:
        op = 0 if '-' in eq else 1
        chars, num = eq.replace('-', '=').split('=')
        lhash = hashme(chars)
        if op == 0:
            lensbox[lhash] = [(ch, n) for (ch, n) in lensbox[lhash] if ch != chars]
        else:
            replaced = False
            for items in range(len(lensbox[lhash])):
                if chars == lensbox[lhash][items][0]:
                    lensbox[lhash][items] = (chars, num)
                    replaced = True
            if not replaced:
                lensbox[lhash].append((chars, num))
    return sum((i + 1) * (j + 1) * int(lensbox[i][j][1]) for i in range(256) for j in range(len(lensbox[i])))

Equations = AoC.Init("data/day15.txt", nolines=True, test=False).split(',')
AoC.verify(511257, 239484)
AoC.run(sum(hashme(eq) for eq in Equations), part_2)
