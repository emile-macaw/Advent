def updateHighest(draw, highestList):
    colorStrings = draw.split(',')
    for colorString in colorStrings:
        amount = int(colorString[1:].split(' ')[0])
        color = colorString[1:].split(' ')[1]

        for highest in highestList:
            if highest[0] == color:
                if(amount > highest[1]):
                    highest[1] = amount
    return highestList

data = open("c:/projects/demo/advent/day2/input.txt")

totalPower = 0

for line in data:
    line = line.replace('\n', '')
    gameId = int(line.split(':')[0][5:])
    draws = line.split(':')[1].split(';')
    
    highest = [['red', 0], ['green', 0], ['blue', 0]]

    for draw in draws:
        highest = updateHighest(draw, highest)      

    totalPower = totalPower + (highest[0][1] * highest[1][1] * highest[2][1])

print(totalPower)
    
