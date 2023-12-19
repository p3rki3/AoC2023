import AoCFramework as AoC
from collections import deque

def accept_reject(part):
    nextrule = 'in'
    while True:
        rule = Rules[nextrule]
        for check in rule.split(','):
            passrule, result = True, check
            if ':' in check:
                condition, result = check.split(':')
                xmas, op, num = condition[0], condition[1], int(condition[2:])
                passrule = part[xmas] > num if op == '>' else part[xmas] < num
            if passrule:
                if result in ['A', 'R']:
                    return result == 'A'
                nextrule = result
                break

def part_1():
    p1answer = 0
    for part in parts.split('\n'):
        part = {p.split('=')[0]:int(p.split('=')[1]) for p in part[1:-1].split(',')}
        if accept_reject(part):
            p1answer += (part['x'] + part['m'] + part['a'] + part['s'])
    return p1answer

def adjust_range(xmas, op, num, minmax):
    idx = 'xmas'.index(xmas)
    match op:
        case '>':
            minmax[2 * idx] = minmax[2 * idx] if minmax[2 * idx] > num + 1 else num + 1
        case '<':
            minmax[2 * idx + 1] = minmax[2 * idx + 1] if minmax[2 * idx + 1] < num - 1 else num - 1
        case 'a':
            minmax[2 * idx + 1] = minmax[2 * idx + 1] if minmax[2 * idx + 1] < num else num
        case 'b':
            minmax[2 * idx] = minmax[2 * idx] if minmax[2 * idx] > num else num
    return minmax

def part_2():
    p2answer, Queue = 0, deque([('in', 1, 4000, 1, 4000, 1, 4000, 1, 4000)])
    while Queue:
        nextrule, xl, xh, ml, mh, al, ah, sl, sh = Queue.pop()
        if nextrule == 'R':
            continue
        elif nextrule == 'A':
            p2answer += (xh - xl + 1) * (mh - ml + 1) * (ah - al + 1) * (sh - sl + 1)
            continue
        else:
            for check in Rules[nextrule].split(','):
                result = check
                if ':' in check:
                    condition, result = check.split(':')
                    xmas, op, num = condition[0], condition[1], int(condition[2:])
                    Queue.append((result, *adjust_range(xmas, op, num, [xl, xh, ml, mh, al, ah,sl, sh])))
                    xl, xh, ml, mh, al, ah, sl, sh = adjust_range(xmas, 'a' if op=='>' else 'b', num, [xl, xh, ml, mh, al, ah,sl, sh])
                else:
                    Queue.append((result, xl, xh, ml, mh, al, ah, sl, sh))
                    break
    return p2answer
   
Rules = {}
rules, parts = AoC.Init("data/day19.txt", nolines=True, test=False).split('\n\n')
for rule in rules.split('\n'):
    Rules[rule.split('{')[0]] = rule.split('{')[1][:-1]
AoC.verify(402185, 130291480568730)
AoC.run(part_1, part_2)
