import AoCFramework as AoC
from functools import cmp_to_key

def part_1():
    sortedDeck = sorted(Deck, key=cmp_to_key(sortme))
    for count, card in enumerate(sortedDeck):
        card[3] = count + 1
    return sum(int(card[1]) * card[3] for card in sortedDeck)

def part_2():
    global Part
    Part = 2
    addons = [[0,0,0,0,0,0,0], [1,2,2,2,0,1,0], [0,2,3,0,2,0,0], [0,0,0,2,2,0,0], [0,0,0,0,0,1,0],[0,0,0,0,0,0,0]]
    for card in Deck:
        jacks = card[0].count('J')
        card[2] += addons[jacks][card[2]]
    return part_1()

def sortme(deck1, deck2):
    (card1, _, rank1, _), (card2, _, rank2, _) = deck1, deck2
    cardlist = 'AKQJT98765432' if Part == 1 else 'AKQT98765432J'
    if rank1 > rank2:
        return 1
    elif rank2 > rank1:
        return -1
    else:
        for c1, c2 in zip(card1, card2):
            _c1, _c2 = cardlist.find(c1), cardlist.find(c2)
            if _c1 > _c2:
                return -1
            elif _c2 > _c1:
                return 1
    print("Ooops.... something is wrong with your sort!")
    exit(1)

def process_file():
    for line in Lines:
        cards, bid = line.split(' ')
        ctype, whichtype = -1, ''
        for card in 'AKQJT98765432':
            if cards.count(card) > 0:
                whichtype += (str(cards.count(card)))
        whichtype = ''.join(sorted(whichtype))
        for count, cardtype in enumerate(['11111', '1112', '122', '113', '23', '14', '5']):
            if whichtype == cardtype:
                ctype = count
        Deck.append([cards, bid, ctype, 0])

Lines, Deck, Part = AoC.Init("data/day7.txt")[0], [], 1
AoC.verify(250602641, 251037509)
process_file()
AoC.run(part_1, part_2)
