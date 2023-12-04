import os

def testDraw(draw, maxAmounts):
    colorStrings = draw.split(',')
    for colorString in colorStrings:
        amount = int(colorString[1:].split(' ')[0])
        color = colorString[1:].split(' ')[1]

        for maxAmount in maxAmounts:
            if maxAmount[0] == color:
                if(amount > maxAmount[1]):
                    return False
    return True

maxAmounts = [['red', 12], ['green', 13], ['blue', 14]]

dir = dir = os.path.dirname(__file__)
data =   open(os.path.join(dir, "input.txt"))

validGameIdSum = 0

for line in data:
    line = line.replace('\n', '')
    gameId = int(line.split(':')[0][5:])
    draws = line.split(':')[1].split(';')
    
    isGameValid = True
    for draw in draws:
        isValid = testDraw(draw, maxAmounts)
        if(not isValid):
            isGameValid = False

    if(isGameValid):
        validGameIdSum = validGameIdSum + gameId

print(validGameIdSum)
    
