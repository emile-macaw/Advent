import os
import re

class MapEntry:
    def __init__(self, sourceLocation, leftLocation, rightLocation):
        self.sourceLocation = sourceLocation
        self.leftLocation = leftLocation
        self.rightLocation = rightLocation

class NavMap:
    def __init__(self):
        self.mapEntries = []        

    def addMapEntry(self, mapEntry:MapEntry):
        self.mapEntries.append(mapEntry)

    def findMapEntry(self, sourceLocation):
        return next((mapEntry for mapEntry in self.mapEntries if mapEntry.sourceLocation == sourceLocation), None)

    def findNextLocation(self, currentLocation, targetDirection):
        mapEntry = self.findMapEntry(currentLocation)
        match targetDirection:
            case 'L':
                return mapEntry.leftLocation
            case 'R':
                return mapEntry.rightLocation

class Navigator:
    def calculateSteps(self, navMap:NavMap, startLocation, goalLocation, routeString):
        stepAmount = 0

        nextLocation = startLocation
        while(nextLocation != goalLocation):
            nextLocation = navMap.findNextLocation(nextLocation, routeString[stepAmount % len(routeString)])
            stepAmount += 1
            print('next ' + nextLocation)

        return stepAmount
    
def parseInput():
    dir = dir = os.path.dirname(__file__)
    data =   open(os.path.join(dir, "input.txt"))

    navMap = NavMap()
    routeString = None

    lineIndex = 0
    for line in data:
        if(lineIndex == 0):
            routeString = line.strip()
        elif lineIndex > 1:
            locations = re.search(r"([A-Z]*) = \(([A-Z]*), ([A-Z]*)\)", line)
            mapEntry = MapEntry(locations.groups()[0], locations.groups()[1], locations.groups()[2])
            navMap.addMapEntry(mapEntry)

        lineIndex += 1    
    return (navMap, routeString)

parseResult = parseInput()

navMap = parseResult[0]
routeString = parseResult[1]

steps = Navigator().calculateSteps(navMap, 'AAA', 'ZZZ', routeString)
print(steps)
    