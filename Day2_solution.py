import AoCFramework as AoC

def part_1():
    idsum = 0
    for game in Games:
        if((game[1] <= 12) and (game[2] <= 13) and (game[3] <= 14)):
            idsum += game[0]
    return idsum

def process_file():
    for line in Lines:
        idt, games = line.split(': ')
        _, idt = idt.split(' ')
        idt = int(idt)
        r, g, b = 0, 0, 0
        for game in games.split('; '):
            for col in game.split(', '):
                num, c = col.split(' ')
                if c == 'blue':
                   b = max(b, int(num))
                elif c == 'green':
                   g = max(g, int(num))
                elif c == 'red':
                   r = max(r, int(num))
        Games.append([idt, r, g, b])

Games, Lines = [], AoC.Init("data/day2.txt")[0]
process_file()
AoC.verify(2679, 77607)
AoC.run(part_1, sum((game[1] * game[2] * game[3]) for game in Games))
