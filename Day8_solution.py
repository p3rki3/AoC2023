import AoCFramework as AoC

def part_1():
    p1answer, curnode, stepptr = 0, 'AAA', 0
    while True:
        p1answer += 1
        nextpair = Nodes[curnode]
        curnode = nextpair[0] if Steps[stepptr] == 'L' else nextpair[1]
        if curnode == 'ZZZ':
            return p1answer
        stepptr = stepptr + 1 if stepptr < len(Steps) - 1 else 0

def gcd(num1, num2):
    while num2:
        num1, num2 = num2, num1%num2
    return num1

def part_2():
    freqs = []
    for curnode in Starts:
        stepcount, stepptr, keepgoing = 0, 0, True
        while keepgoing:
            stepcount += 1
            nextpair = Nodes[curnode]
            curnode = nextpair[0] if Steps[stepptr] == 'L' else nextpair[1]
            if curnode in Ends:
                freqs.append(stepcount)
                keepgoing = False
            stepptr = stepptr + 1 if stepptr < len(Steps) - 1 else 0
    p2answer = 1
    for freq in freqs:
        p2answer = (p2answer * freq) // gcd(p2answer, freq)
    return p2answer
   
def process_file():
    global Steps, Nodes
    Steps = Lines[0]
    for line in Lines[2:]:
        n, m = line.split(' = ')
        l, r = m[1:-1].split(', ')
        Nodes[n] = (l, r)
        if n.endswith('A'):
            Starts.append(n)
        if n.endswith('Z'):
            Ends.append(n)


Lines = AoC.Init("data/day8.txt")[0]
Steps, Nodes, Starts, Ends = [], dict(), [], []
process_file()
AoC.verify(17263, 14631604759649)
AoC.run(part_1, part_2)
