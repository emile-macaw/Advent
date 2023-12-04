import re

data = open("c:/projects/demo/advent/day3/input.txt")


lines = []
for ioLine in data:
    lines.append(ioLine.replace('\n', ''))


lineIndex = 0

docSum = 0

for line in lines:
    numberStrings = re.finditer(r'\d+', line)
    
    lineSum = 0

    for numberString in numberStrings:
        startPos = numberString.start() - 1 if numberString.start() > 1 else 0
        endPos = numberString.end() + 1 if numberString.end() < len(line) - 1 else len(line) - 1
        
        hasMatch = False
        
        if lineIndex > 0:
            print('matching' + lines[lineIndex - 1][startPos:endPos])
            if re.search(r"[^\d\.]", lines[lineIndex - 1][startPos:endPos]):
                hasMatch = True
        
        print('matching' + line[startPos:endPos])
        if re.search(r"[^\d\.]", line[startPos:endPos]):
            hasMatch = True

        if lineIndex < len(lines) - 1:
            print('matching' + lines[lineIndex + 1][startPos:endPos])
            if re.search(r"[^\d\.]", lines[lineIndex + 1][startPos:endPos]):
                hasMatch = True

        if hasMatch:
            lineSum += int(numberString.group())

        print('line sum ' + str(lineSum))

    docSum += lineSum
    lineIndex += 1

    print('doc sum ' + str(docSum))


    