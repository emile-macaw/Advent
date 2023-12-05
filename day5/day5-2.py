import os
import re
from typing import List

dir = dir = os.path.dirname(__file__)
data =   open(os.path.join(dir, "input.txt"))

class indexRange:
    def __init__(self, startIndex, length):
        self.startIndex = int(startIndex)
        self.length = int(length)

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
    
    def getMaxLengthAvailableFromStartIndex(self, sourceIndex) -> int:
        offset = sourceIndex - self.sourceIndexRangeStart
        lengthAvailable = self.length - offset
        return lengthAvailable
    
    def translateRangeToTargetIndex(self, sourceIndexRange:indexRange) -> indexRange:
        offset = self.targetIndexRangeStart - self.sourceIndexRangeStart
        maxLengthAvailable = self.getMaxLengthAvailableFromStartIndex(sourceIndexRange.startIndex)
        targetRangeStartIndex = sourceIndexRange.startIndex + offset
        targetRangeLength = sourceIndexRange.length if maxLengthAvailable > sourceIndexRange.length else maxLengthAvailable
        targetRange = indexRange(targetRangeStartIndex, targetRangeLength)
        return targetRange

class almanacMap:

    def __init__(self, sourceType, targetType):
        self.mapEntries = []
        self.sourceType = sourceType
        self.targetType = targetType

    def addMapping(self, sourceIndex, targetIndex, length):
        self.mapEntries.append(almanacMapEntry(sourceIndex, targetIndex, length))

    def findEntryForSourceIndex(self, sourceIndex):
        return next((mapEntry for mapEntry in self.mapEntries if mapEntry.isInRange(sourceIndex)), None)
    
    def findNextMapEntryFromStartIndex(self, sourceIndex):
        closestMapEntry = None
        for mapEntry in self.mapEntries:
            if(mapEntry.sourceIndexRangeStart > sourceIndex and (closestMapEntry == None or mapEntry.sourceIndexRangeStart < closestMapEntry.sourceIndexRangeStart)):
                closestMapEntry = mapEntry
        return closestMapEntry

    def findTargetIndex(self, sourceIndex) -> int:
        matchingEntry =  self.findEntryForSourceIndex(sourceIndex)
        
        if(matchingEntry):
            return matchingEntry.determineTargetIndex(sourceIndex)
        else:
            return sourceIndex
        
    def getNextIndexRanges(self, sourceIndexRange:indexRange): 
        
        indexRanges = []
        
        startIndex = sourceIndexRange.startIndex
        indexLength = sourceIndexRange.length
        entryForStartIndex = self.findEntryForSourceIndex(startIndex)

        if entryForStartIndex != None:
            indexRanges.append(entryForStartIndex.translateRangeToTargetIndex(sourceIndexRange))

            maxLengthAvailableInEntry = entryForStartIndex.getMaxLengthAvailableFromStartIndex(startIndex)

            if(maxLengthAvailableInEntry < indexLength):
                nextStartIndex = startIndex + maxLengthAvailableInEntry
                nextLength = indexLength - maxLengthAvailableInEntry
                nextIndexRange = indexRange(nextStartIndex, nextLength)
                indexRanges.extend(self.getNextIndexRanges(nextIndexRange))
        else:
            #handle non-defined entry, also in case its range overlaps with a defined map
            closestMapEntry = self.findNextMapEntryFromStartIndex(startIndex)
            lengthAvailableBeforeClosestMapEntry = closestMapEntry.sourceIndexRangeStart - startIndex if closestMapEntry != None else indexLength
            indexRanges.append(indexRange(startIndex, lengthAvailableBeforeClosestMapEntry))

            if(closestMapEntry != None):
                nextStartIndex = startIndex + lengthAvailableBeforeClosestMapEntry
                nextLength = indexLength - lengthAvailableBeforeClosestMapEntry
                nextIndexRange = indexRange(nextStartIndex, nextLength)
                indexRanges.extend(self.getNextIndexRanges(nextIndexRange))

        return indexRanges;        


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


def processIndexRanges(startIndexRange):
    closestLocation = -1
    
    currentMapName = 'seed'
    currentIndexRanges = [startIndexRange]

    while almanac.findMap(currentMapName) != None:
        currentMap = almanac.findMap(currentMapName)        
        nextIndexRanges = []

        print('current map is ' + currentMap.sourceType)
        
        for currentIndexRange in currentIndexRanges:
            print('processing index range ' + str(currentIndexRange.startIndex) + ' - ' + str(currentIndexRange.length))
            nextIndexRanges.extend(currentMap.getNextIndexRanges(currentIndexRange))

        currentMapName = currentMap.targetType
        currentIndexRanges = nextIndexRanges

    for indexRange in currentIndexRanges:
        print('determine final index range ' + str(indexRange.startIndex) + ' - ' + str(indexRange.length))
        if closestLocation == -1 or indexRange.startIndex < closestLocation:
            closestLocation = indexRange.startIndex

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


#puzzle 2
closestLocation = -1

for index in range(int(len(seedNumbers) / 2)):
    seedNumberStart = int(seedNumbers[index * 2])
    seedNumberLength = int(seedNumbers[index * 2 + 1])

    startIndexRange = indexRange(seedNumberStart, seedNumberLength)
     
    rangeClosestLocation = processIndexRanges(startIndexRange)
    if rangeClosestLocation < closestLocation or closestLocation == -1:
        closestLocation = rangeClosestLocation


print('Closest location ' + str(closestLocation))
