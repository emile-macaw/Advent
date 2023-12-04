import os
import re

dir = dir = os.path.dirname(__file__)
data =   open(os.path.join(dir, "input.txt"))


lines = []
for ioLine in data:
    lines.append(ioLine.replace('\n', ''))

numbers = []

lineIndex = 0
for line in lines:
    numberStrings = re.finditer(r'\d+', line)
    
    lineSum = 0

    for numberString in numberStrings:
        startPos = numberString.start()
        endPos = numberString.end() -1
        number = int(numberString.group())

        numbers.append([lineIndex, startPos, endPos, number])

    lineIndex += 1
       
lineIndex = 0

totalGearSum = 0
for line in lines:
    gears = re.finditer(r'\*', line)

    lineGearSum = 0

    for gear in gears:

        gearIndex = gear.start()

        adjNumbers = []
        for number in numbers:
            numLine = number[0]
            startPos = number[1]
            endPos = number[2]            
            if (numLine >= lineIndex - 1 and numLine <= lineIndex + 1 ) and ((startPos >= gearIndex - 1 and startPos <= gearIndex + 1) or (endPos >= gearIndex -1 and endPos <= gearIndex + 1)):
                adjNumbers.append(number[3])

        if len(adjNumbers) == 2:
            lineGearSum += (adjNumbers[0] * adjNumbers[1])

        print('line ' + str(lineGearSum))            

    totalGearSum += lineGearSum
    print('total ' + str(totalGearSum))
    lineIndex += 1


    