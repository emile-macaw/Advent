import os
import re

dir = dir = os.path.dirname(__file__)
data =   open(os.path.join(dir, "input.txt"))

score = 0

lines = []
for lineIO in data:
    lines.append(lineIO)

# create one card of each to begin with
cardAmounts = []

for line in lines:
    cardAmounts.append(1)

# process lines
lineIndex = 0
for line in lines:
    cardNumberString = line.split(':')[0]
    winningNumbersString = line.split(':')[1].split('|')[0]
    ownedNumbersString = line.split('|')[1]

    cardNumber = int(re.findall(r"\d+", cardNumberString)[0])
    winningNumbers = re.findall(r"\d+", winningNumbersString)
    ownedNumbers = re.findall(r"\d+", ownedNumbersString)

    winAmount = 0
    for ownedNumber in ownedNumbers:
        for winningNumber in winningNumbers:
            if(ownedNumber == winningNumber):
                winAmount += 1

    for nextCardIndex in range(lineIndex + 1, lineIndex + 1 + winAmount):           
        cardAmounts[nextCardIndex] += cardAmounts[lineIndex]
        
    lineIndex += 1

totalCards = 0
for cardAmount in cardAmounts:
    totalCards += cardAmount

print(totalCards)