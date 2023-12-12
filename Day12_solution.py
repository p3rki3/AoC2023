import AoCFramework as AoC

def solve(spring, condrecs):
    result = 0
    if (spring, condrecs) in Cache:
        return Cache[(spring, condrecs)]
    chk = 1 if condrecs == () else 0
    if not spring:
        return chk
    if chk:
        if '#' in spring:
            return 0
        return 1
    if spring[0] in '.?':
        result += solve(spring[1:], condrecs)
    if spring[0] in '#?':
        if '.' not in spring[:condrecs[0]] and condrecs[0] <= len(spring) and (condrecs[0] == len(spring) or spring[condrecs[0]] != '#'):
            result += solve(spring[condrecs[0] + 1:], condrecs[1:])
    Cache[(spring, condrecs)] = result
    return result

p1answer = p2answer = 0
for line in AoC.Init('data/day12.txt')[0]:
    Cache = {}
    Springs, Condrecs = line.split(' ')
    Condrecs = tuple(int(num) for num in Condrecs.split(','))
    p1answer += solve(Springs, Condrecs)
    Springs = '?'.join([Springs] * 5)
    Condrecs *= 5
    p2answer += solve(Springs, Condrecs)

AoC.verify(7236, 11607695322318)
AoC.run(p1answer, p2answer)
