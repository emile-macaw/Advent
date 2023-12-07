import os
from collections import Counter

cardsByValues = "23456789TJQKA"

class hand:    

    def __init__(self, cardString:str, bid:int):
        self.cardString = cardString
        self.bid = bid
    
    def getSetSizes(self):
        counter = Counter(self.cardString)
        values = list(map(lambda d: d, counter.values()))        
        return sorted(values, reverse=True)

    def getSortableValue(self):
        print('calculate value for hand ' + self.cardString)

        totalCardValue = 0
        cardPos = 1
        
        for card in self.cardString:
            cardValue = (cardsByValues.index(card) + 1) *  (len(cardsByValues) + 1) ** (len(self.cardString) + 1 - cardPos)
            totalCardValue += cardValue
            cardPos += 1

            print('card ' + card + ' at pos ' + str(cardPos) + ' gets value ' + str(cardValue))

        setSizes = self.getSetSizes()
        primarySizeValue = setSizes[0] * (len(cardsByValues) + 1) ** (len(self.cardString) + 2)
        print('primary size value ' + str(primarySizeValue))
        secondarySizeValue = setSizes[1] * (len(cardsByValues) + 1) ** (len(self.cardString) + 1) if len(setSizes) > 1 else 0
        print('secondary size value ' + str(secondarySizeValue))

        sortableValue = primarySizeValue + secondarySizeValue + totalCardValue

        print('total value ' + str(sortableValue))

        return sortableValue        

def parseInput():

    dir = dir = os.path.dirname(__file__)
    data =   open(os.path.join(dir, "input.txt"))

    hands = []
    for line in data:
        cardString = line.split(' ')[0]
        bid = int(line.split(' ')[1])
        hands.append(hand(cardString, bid))
    return hands

hands = parseInput()
hands.sort(key = lambda h:h.getSortableValue())

rankIndex = 1
totalRank = 0
for hand in hands:
    totalRank += hand.bid * rankIndex
    print('hand with cards ' + hand.cardString + ' index ' + str(rankIndex) + ' bid ' + str(hand.bid) + ' rank ' + str(totalRank))
    rankIndex += 1

print(totalRank)
