import os
import sys

class gridLocation:

    stepsFromStart = -1

    def __init__(self, line, col, symbol):
        self.line = line
        self.col = col
        self.symbol = symbol

class grid:

    locations = []

    def addLocation(self, location:gridLocation):
        self.locations.append(location)

    def findStartLocation(self):
        return next(location for location in self.locations if location.symbol == 'S')
    
    def findLocation(self, line:int, col:int):
        return next((location for location in self.locations if location.line == line and location.col == col), None)
    
    def updateNeighbours(self, location:gridLocation, stepsFromStart):

        print('updating loc ' + str(location.line) + ':' + str(location.col) + ' sym ' + location.symbol + ' newsteps ' + str(stepsFromStart) + ' oldsteps ' + str(location.stepsFromStart))

        if stepsFromStart < location.stepsFromStart or location.stepsFromStart == -1:                        
            location.stepsFromStart = stepsFromStart
            
            neighbours = []
            match location.symbol:
                case '|':
                    neighbours.append(self.findLocation(location.line - 1, location.col))
                    neighbours.append(self.findLocation(location.line + 1, location.col))
                case '-':
                    neighbours.append(self.findLocation(location.line, location.col - 1))
                    neighbours.append(self.findLocation(location.line, location.col + 1))
                case 'L':
                    neighbours.append(self.findLocation(location.line - 1, location.col))
                    neighbours.append(self.findLocation(location.line, location.col + 1))
                case 'J':
                    neighbours.append(self.findLocation(location.line - 1, location.col))
                    neighbours.append(self.findLocation(location.line, location.col -1))
                case '7':
                    neighbours.append(self.findLocation(location.line, location.col -1))
                    neighbours.append(self.findLocation(location.line + 1, location.col))
                case 'F':
                    neighbours.append(self.findLocation(location.line, location.col + 1))
                    neighbours.append(self.findLocation(location.line + 1, location.col))
                case 'S':
                    leftLoc = self.findLocation(location.line, location.col - 1)
                    rightLoc = self.findLocation(location.line, location.col + 1)
                    topLoc = self.findLocation(location.line - 1, location.col) 
                    bottomLoc = self.findLocation(location.line + 1, location.col)
                    
                    if(leftLoc != None and leftLoc.symbol in ['-', 'F', 'L']): neighbours.append(leftLoc)
                    if(rightLoc != None and rightLoc.symbol in ['-', 'J', '7']): neighbours.append(rightLoc)
                    if(topLoc != None and topLoc.symbol in ['|', '7', 'F']): neighbours.append(topLoc)
                    if(bottomLoc != None and bottomLoc.symbol in ['|', 'J', 'L']): neighbours.append(bottomLoc)                    

            for neighbour in neighbours:
                self.updateNeighbours(neighbour, stepsFromStart + 1)
   
    def findMaxSteps(self):
        maxSteps = max(list(map(lambda l: l.stepsFromStart ,self.locations)))
        return maxSteps

def parseInput():
    dir = dir = os.path.dirname(__file__)
    data =   open(os.path.join(dir, "input.txt"))

    parsedGrid = grid()

    lineIndex = 0
    for line in data:
        line = line.strip()
        colIndex = 0
        for col in line:
            parsedGrid.addLocation(gridLocation(lineIndex, colIndex, col))
            colIndex += 1
        
        lineIndex += 1

    return parsedGrid

sys.setrecursionlimit(20000)

pipesGrid = parseInput()

startLocation = pipesGrid.findStartLocation()
pipesGrid.updateNeighbours(startLocation, 0)
print(pipesGrid.findMaxSteps())


