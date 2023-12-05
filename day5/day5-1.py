import os
import re
from typing import List

dir = dir = os.path.dirname(__file__)
data =   open(os.path.join(dir, "input.txt"))

class almanacMapEntry:
    def __init__(self, sourceIndexRangeStart, targetIndexRangeStart, length):
        self.sourceIndexRangeStart = int(sourceIndexRangeStart)
        self.targetIndexRangeStart = int(targetIndexRangeStart)
        self.length = int(length)

    def isInRange(self, sourceIndex) -> bool:
        isInrange = self.sourceIndexRangeStart <= sourceIndex and self.sourceIndexRangeStart + self.length > sourceIndex
        return isInrange
    
    def determineTargetIndex(self, sourceIndex) -> int:
        offset = sourceIndex - self.sourceIndexRangeStart
        return self.targetIndexRangeStart + offset

class almanacMap:

    def __init__(self, sourceType, targetType):
        self.mapEntries = []
        self.sourceType = sourceType
        self.targetType = targetType

    def addMapping(self, sourceIndex, targetIndex, length):
        self.mapEntries.append(almanacMapEntry(sourceIndex, targetIndex, length))

    def findTargetIndex(self, sourceIndex) -> int:
        matchingEntry = next((mapEntry for mapEntry in self.mapEntries if mapEntry.isInRange(sourceIndex)), None)
        
        if(matchingEntry):
            return matchingEntry.determineTargetIndex(sourceIndex)
        else:
            return sourceIndex

class almanac:

    def __init__(self):
        self.maps = []

    def addMap(self, map):
        self.maps.append(map)

    def findMap(self, sourceType) -> almanacMap:
        return next((map for map in self.maps if map.sourceType == sourceType), None)  
    
    def hasNextMap(self, sourceType) -> bool:
        currentMap = self.findMap(sourceType)
        targetType = currentMap.targetType
        return self.findMap(targetType) != None


def processNumbers(seedNumbers):
    closestLocation = -1

    for seedNumber in seedNumbers:

        print('Processing seed ' + str(seedNumber))

        nextMapName = 'seed'
        nextTargetNumber = int(seedNumber)

        while almanac.findMap(nextMapName) != None:
            
            print('Finding source number ' + str(nextTargetNumber) + ' in map ' + str(nextMapName))

            currentMap = almanac.findMap(nextMapName)        
            nextTargetNumber = currentMap.findTargetIndex(nextTargetNumber)

            print('Found target number ' + str(nextTargetNumber))

            nextMapName = currentMap.targetType

        locationForSeed = nextTargetNumber

        if locationForSeed < closestLocation or closestLocation == -1:
            closestLocation = locationForSeed

    return closestLocation



seedNumbers = []

almanac = almanac()
currentMap = None

#parse document, create almanac
for line in data:
    
    #seeds line
    if line.startswith('seeds:'):
        seedNumbers = re.findall(r"\d+", line)
        continue

    # map header line
    matchesMapHeader = re.search(r"(.*)-to-(.*) map:", line)
    if(matchesMapHeader):
        fromType = matchesMapHeader.groups()[0]
        toType = matchesMapHeader.groups()[1]
        
        currentMap = almanacMap(fromType, toType)
        almanac.addMap(currentMap)

        continue

    # map entries
    mapEntries = re.findall(r"\d+", line)
    if mapEntries:
        currentMap.addMapping(mapEntries[1], mapEntries[0], mapEntries[2])     



#puzzle 1
closestLocation = processNumbers(seedNumbers)
print('Closest location 1' + str(closestLocation))

