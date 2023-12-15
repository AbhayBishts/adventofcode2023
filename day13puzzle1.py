def findHorizontalReflection(puzzleMap):
    possibleReflectionValues = set()
    possibleReflectionValues.add(0)

    for i in range(len(puzzleMap)-1):
        if puzzleMap[i] == puzzleMap[i+1]:
            firstIndex = i
            secondIndex = i+1

            distanceFromStart = firstIndex - 0
            distanceFromEnd = len(puzzleMap) - secondIndex - 1
            
            numberOfLinesToCheck = min(distanceFromStart, distanceFromEnd)
            matchingLines = 0

            for i in range(1,numberOfLinesToCheck+1):
                if (puzzleMap[firstIndex-i] == puzzleMap[secondIndex+i]):
                    matchingLines += 1
        
            if matchingLines == numberOfLinesToCheck:
                possibleReflectionValues.add(100 * (firstIndex + 1))
    
    return max(possibleReflectionValues)

def getColumn(puzzleMap, index):
    column = []
    for row in puzzleMap:
        column.append(row[index])
    return column

def findVerticalReflection(puzzleMap):
    possibleReflectionValues = set()
    possibleReflectionValues.add(0)

    prevColumn = getColumn(puzzleMap, 0)
    for i in range(1,len(puzzleMap[0])):
        currColumn = getColumn(puzzleMap, i)
        if (currColumn == prevColumn):
            firstIndex = i - 1
            secondIndex = i

            distanceFromStart = firstIndex - 0
            distanceFromEnd = len(puzzleMap[0]) - secondIndex - 1
            
            numberOfLinesToCheck = min(distanceFromStart, distanceFromEnd)
            matchingLines = 0

            for i in range(1,numberOfLinesToCheck+1):
                if (getColumn(puzzleMap, firstIndex - i) == getColumn(puzzleMap, secondIndex + i)):
                    matchingLines += 1
            
            if matchingLines == numberOfLinesToCheck:
                possibleReflectionValues.add(firstIndex + 1)
        else:
            prevColumn = currColumn

    return max(possibleReflectionValues)

def findReflection(puzzleMap):
    returnSum = 0
    returnSum += findHorizontalReflection(puzzleMap)
    returnSum += findVerticalReflection(puzzleMap)
    return returnSum

def findSumOfReflections():
    totalSum = 0
    with open('./day13input.txt', 'r') as file:
        puzzleMap = []

        for line in file:
            if line != '\n':
                characters = []
                for char in line:
                    if (char != '\n'):
                        characters.append(char)
                puzzleMap.append(characters)
            else:
                totalSum += findReflection(puzzleMap)
                puzzleMap = []
        
        totalSum += findReflection(puzzleMap)
        
    print(totalSum)

if __name__ == "__main__":
    findSumOfReflections()