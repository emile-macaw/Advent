import os
import re

dir = dir = os.path.dirname(__file__)
data =   open(os.path.join(dir, "input.txt"))

def prependPreviousNumber(numbers:[]):
    diff = [j-i for i,j in (zip(numbers[:-1], numbers[1:]))]
    
    if len(list(number for number in diff if number != 0)) > 0:
        nextRange = prependPreviousNumber(diff)    
        print(nextRange)
        numbers.insert(0, numbers[0] - nextRange[0])
    
    return numbers


total = 0
for line in data:
    numbers = list(map(lambda n: int(n), re.findall(r"-?\d+", line)))
    numbersWithPrev = prependPreviousNumber(numbers)    
    total += numbersWithPrev[0]
    print(numbersWithPrev)
print(total)
