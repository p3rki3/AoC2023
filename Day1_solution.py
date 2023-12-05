import AoCFramework as AoC
import re

def answer(line):
    digits = re.findall(r'\d', line)
    return int(digits[0] + digits[-1])

p1answer = p2answer = 0
AoC.verify(53080, 53268)
for line in AoC.Init("data/day1.txt")[0]:
    p1answer += answer(line)
    for count, numeral in enumerate(['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']):
        line = line.replace(numeral, numeral[0] + str(count+1) + numeral[-1])
    p2answer += answer(line)
AoC.run(p1answer, p2answer)
