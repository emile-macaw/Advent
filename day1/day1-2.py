import os
import re

dir = dir = os.path.dirname(__file__)
data =   open(os.path.join(dir, "input.txt"))

processedLines = 0
sum = 0

numberDict = [ ['one', '1'], ['two', '2'], ['three', '3'], ['four', '4'], ['five', '5'], ['six', '6'], ['seven', '7'], ['eight', '8'], ['nine', '9'] ]

def findNumberAtPos(pos, line):   

    number = ''

    if re.match(r"\d", line[pos]):
        number = line[pos]
    else:
        sub = line[pos:]
        for dictEntry in numberDict:
            dictKey = dictEntry[0]
            dictVal = dictEntry[1]
            if sub.startswith(dictKey):
                number = dictVal
                break
    
    return number


for line in data:
    for i in range(len(line)):
        number = findNumberAtPos(i, line)
        if(number != ''):
            firstNumber = number
            break;

    for i in reversed(range(len(line))):
        number = findNumberAtPos(i, line)
        if(number != ''):
            lastNumber = number
            break;
    
    print(line)
    print(firstNumber + '-' + lastNumber)
    
    combinedNumber = firstNumber + lastNumber

    print(combinedNumber)
    sum = sum + int(combinedNumber)

    processedLines = processedLines + 1

print(processedLines)
print(sum)
