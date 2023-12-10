import os
import re

dir = dir = os.path.dirname(__file__)
data =   open(os.path.join(dir, "input.txt"))

def appendNextNumber(numbers:[]):
    diff = [j-i for i,j in (zip(numbers[:-1], numbers[1:]))]
    
    if len(list(number for number in diff if number != 0)) > 0:
        nextRange = appendNextNumber(diff)    
        numbers.append(numbers[-1] + nextRange[-1])
    
    return numbers

total = 0
for line in data:
    numbers = list(map(lambda n: int(n), re.findall(r"-?\d+", line)))
    numbersWithNext = appendNextNumber(numbers)    
    total += numbersWithNext[-1]
    print(numbersWithNext)
print(total)
