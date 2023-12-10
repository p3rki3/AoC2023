import AoCFramework as AoC
from collections import deque

def myneighbours(i, j, maxi, maxj):
    return [(i, j) for i, j in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)] if 0 <= i < maxi and 0 <= j < maxj]

def fltr(board, points):
    return points if Part == 2 else [(i,j) for i,j in points if i < len(board) and j < len(board[0]) and i >= 0 and j >= 0]

def isnextto(board, i, j, a, b):
    if board[a][b] == '.':
        return []
    elif board[a][b] == '|':
        return fltr(board, [(i-1, j), (i+1, j)])
    elif board[a][b] == '-':
        return fltr(board, [(i, j-1), (i, j+1)])
    elif board[a][b] == 'L':
        return fltr(board, [(i-1, j), (i, j+1)])
    elif board[a][b] == 'J':
        return fltr(board, [(i, j-1), (i-1, j)])
    elif board[a][b] == '7':
        return fltr(board, [(i+1, j), (i, j-1)])
    elif board[a][b] == 'F':
        return fltr(board, [(i, j+1), (i+1, j)])
    elif board[a][b] == 'S':
        return [(ii, jj) for ii, jj in myneighbours(i, j, len(board), len(board[0])) if (i, j) in isnextto(board, ii, jj, ii, jj)]
    print("Oooooopsie - don't understand this board; should never have gotten here; stopping now!")
    exit(1)

def part_1():
    global Found, Startcoord
    for r, line in enumerate(Lines):
        for c, ch in enumerate(line):
            if ch == 'S':
                Startcoord = (r,c)
    (i, j) = Startcoord
    found, queue = set([(i, j)]), deque([(i, j)])
    while len(queue) > 0:
        i, j = queue.popleft()
        for neighbours in isnextto(Lines, i, j, i, j):
            if neighbours not in found and Lines[neighbours[0]][neighbours[1]] != '.':
                queue.append(neighbours)
                found.add(neighbours)
    Found = found
    return len(found) // 2

def part_2():
    global Part
    (i,j), Part, maxi, maxj = Startcoord, 2, len(Lines) * 2, len(Lines[0]) * 2
    points, points2 = [(2 * i, 2 * j) for i, j in Found], []
    for ii, jj in points:
        iii, jjj = ii // 2, jj // 2
        for neighbour in isnextto(Lines, ii, jj, iii, jjj):
            points2.append(neighbour)
    checkpoints = set(points + points2)
    starts = set([(2 * i + 1, 2 * j + 1), (2 * i - 1, 2 * j + 1), (2 * i + 1, 2 * j - 1), (2 * i - 1, 2 * j - 1)])
    for start in starts:
        visited, queue, dontanswer = set([start]), deque([start]), False
        while(len(queue) > 0):
            i, j = queue.popleft()
            for neighbour in myneighbours(i, j, maxi, maxj):
                if neighbour in checkpoints:
                    continue
                if neighbour == (0,0):
                    dontanswer = True
                    break
                if neighbour not in visited:
                    queue.append(neighbour)
                    visited.add(neighbour)
        if not dontanswer:
            return sum(1 for i, j in visited if i % 2 == 0 and j % 2 == 0)
    return("Couldn't find a solution!")

Part, Found, Startcoord, Lines = 1, None, None, AoC.Init("data/day10.txt")[0]
AoC.verify(6856, 501)
AoC.run(part_1, part_2)