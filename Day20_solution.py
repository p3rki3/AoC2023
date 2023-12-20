import AoCFramework as AoC
from collections import defaultdict, deque
from math import gcd

def solve():
    p2answer, lohi, Types, Conns, Fromnode, Invstate = 1, [0, 0], {}, {}, {}, defaultdict(list)
    for line in Lines:
        left, right = line.split('->')
        right = right.strip().split(', ')
        Conns[left[:-1]] = right
        Types[left[1:-1]] = left[0]
    for lhs, rhslist in Conns.items():
        Conns[lhs] = [Types[rhs] + rhs if rhs in Types else rhs for rhs in rhslist]
        for node in Conns[lhs]:
            if node[0] == '&':
                Fromnode[node] = {} if node not in Fromnode else Fromnode[node]
                Fromnode[node][lhs] = False     # False = low state, True = high
            Invstate[node].append(lhs)
    Watchlist, Queue, Onstate, Prevstate, Counter, P2factors = Invstate[Invstate['rx'][0]], deque(), set(), {}, defaultdict(int), []
    for pushbutton in range(1, 50000):
        Queue.append(('broadcaster', 'button', False))
        while Queue:
            tonode, fromnode, state = Queue.popleft()
            if not state:
                if tonode in Prevstate and Counter[tonode] == 2 and tonode in Watchlist:
                    P2factors.append(pushbutton - Prevstate[tonode])
                    if len(P2factors) == len(Watchlist):
                        for num in P2factors:
                            p2answer = (p2answer * num) // gcd(num , p2answer)
                        print('Part 2 answer found in ', pushbutton, ' cycles\n')
                        return lohi[0] * lohi[1], p2answer
                Prevstate[tonode] = pushbutton
                Counter[tonode] += 1
            lohi[state] += 1 if pushbutton < 1001 else 0
            if tonode[0] == '%':
                if state:
                    continue
                if tonode not in Onstate:
                    Onstate.add(tonode)
                    newstate = True
                else:
                    Onstate.discard(tonode)
                    newstate = False
                for node in Conns[tonode]:
                    Queue.append((node, tonode, newstate))
            elif tonode[0] == '&':
                Fromnode[tonode][fromnode] = state
                newstate = (False if all(state1 for state1 in Fromnode[tonode].values()) else True)
                for node in Conns[tonode]:
                    Queue.append((node, tonode, newstate))
            elif tonode == 'broadcaster':
                for node in Conns[tonode]:
                    Queue.append((node, tonode, state))
            elif tonode not in Conns:
                continue

Lines = AoC.Init("data/day20.txt", test=False)[0]
AoC.verify(711650489, 219388737656593)
AoC.run(solve)
