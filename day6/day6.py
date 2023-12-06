import os
import re

dir = dir = os.path.dirname(__file__)
data =   open(os.path.join(dir, "input.txt"))

times = []
bestDistances = []
for line in data:
    if line.startswith('Time:'):
        times = re.findall(r"\d+", line)
    if line.startswith('Distance:'):
        bestDistances = re.findall(r"\d+", line)

timeIndex = 0

totalWaysToBeat = []

for time in times:
    
    countWaysToBeat = 0

    for attemptMs in range(int(time) + 1):
        distance = (int(time) - attemptMs) * attemptMs
        bestDistance = int(bestDistances[timeIndex])
        if distance > bestDistance:
            countWaysToBeat += 1

    totalWaysToBeat.append(countWaysToBeat)
    timeIndex += 1

mulWaysToBeat = 1
for totalWayToBeat in totalWaysToBeat:
    mulWaysToBeat *= totalWayToBeat

print ('Multiplied ways to beat ' + str(mulWaysToBeat))