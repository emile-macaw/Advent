import os
import re

dir = dir = os.path.dirname(__file__)
data =   open(os.path.join(dir, "input.txt"))

processedLines = 0
sum = 0

for line in data:
    justNumbers = re.findall(r"\d", line)
    
    print(line)
    print(justNumbers)

    firstNumber = justNumbers[0]
    combinedNumber = firstNumber

    lastNumber = justNumbers[len(justNumbers)-1]
    combinedNumber = combinedNumber + lastNumber

    print(combinedNumber)
    sum = sum + int(combinedNumber)

    processedLines = processedLines + 1

print(processedLines)
print(sum)
