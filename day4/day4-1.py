import os
import re

dir = dir = os.path.dirname(__file__)
data =   open(os.path.join(dir, "input.txt"))

score = 0

for line in data:
    winningNumbersString = line.split(':')[1].split('|')[0]
    ownedNumbersString = line.split('|')[1]

    winningNumbers = re.findall(r"\d+", winningNumbersString)
    ownedNumbers = re.findall(r"\d+", ownedNumbersString)

    lineScore = 0

    for ownedNumber in ownedNumbers:
        for winningNumber in winningNumbers:
            if(ownedNumber == winningNumber):
                lineScore = lineScore * 2 if lineScore > 0 else 1

    score += lineScore
        
    print('Score:' + str(score))