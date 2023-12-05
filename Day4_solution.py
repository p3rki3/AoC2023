import AoCFramework as AoC

def part_1():
    for card in Cards:
        for n in card[1]:
            if n in card[2]:
                card[3] += 1
    return int(sum((2 ** (card[3] - 1)) for card in Cards if card[3] > 0))

def part_2():
    for i in range(len(Cards)):
        if Cards[i][3] > 0:
            for j in range(Cards[i][3]):
                Cards[i+j+1][4] += Cards[i][4]
    return sum(card[4] for card in Cards)

Cards = []
AoC.verify(24160, 5659035)
for count, line in enumerate(AoC.Init("data/day4.txt")[0]):
    mynums_t, winnums_t = line.split(':')[1].split('|')
    mynums = [int(n) for n in mynums_t.strip().replace('  ', ' ').split(' ')]
    winnums = [int(n) for n in winnums_t.strip().replace('  ', ' ').split(' ')]
    Cards.append([count, mynums, winnums, 0, 1])
AoC.run(part_1, part_2)
