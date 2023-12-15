oldReflectionIndicesVertical = dict()
oldReflectionIndicesHorizontal = dict()

def compareWithSmudge(array1,array2):
    totalMatches = 0
    for i in range(len(array1)):
        if array1[i] == array2[i]:
            totalMatches += 1
    return totalMatches == len(array1) - 1

def findHorizontalReflection(puzzleMap, puzzleIndex, smudge):
    global oldReflectionIndicesHorizontal
    possibleReflectionValues = dict()
    possibleReflectionValues[0] = -1

    for i in range(len(puzzleMap)-1):
        smudgeExists = False
        piecesEquivalent = puzzleMap[i] == puzzleMap[i+1]
        if (not piecesEquivalent) and (not smudgeExists and smudge) and compareWithSmudge(puzzleMap[i], puzzleMap[i+1]):
            piecesEquivalent = True
            smudgeExists = True

        if piecesEquivalent:
            firstIndex = i
            secondIndex = i+1

            if (puzzleIndex in oldReflectionIndicesHorizontal and oldReflectionIndicesHorizontal[puzzleIndex] == firstIndex):
                continue

            distanceFromStart = firstIndex - 0
            distanceFromEnd = len(puzzleMap) - secondIndex - 1
            
            numberOfLinesToCheck = min(distanceFromStart, distanceFromEnd)
            matchingLines = 0

            for i in range(1,numberOfLinesToCheck+1):
                if (puzzleMap[firstIndex-i] == puzzleMap[secondIndex+i]):
                    matchingLines += 1
                elif (not smudgeExists and smudge) and compareWithSmudge(puzzleMap[firstIndex-i], puzzleMap[secondIndex+i]):
                    matchingLines += 1
                    smudgeExists = True
        
            if matchingLines == numberOfLinesToCheck:
                possibleReflectionValues[(100 * (firstIndex + 1))] = firstIndex
    
    maxReflectionValue = max(possibleReflectionValues.keys())
    if (puzzleIndex not in oldReflectionIndicesHorizontal):
        oldReflectionIndicesHorizontal[puzzleIndex] = possibleReflectionValues[maxReflectionValue]

    return maxReflectionValue

def getColumn(puzzleMap, index):
    column = []
    for row in puzzleMap:
        column.append(row[index])
    return column

def findVerticalReflection(puzzleMap, puzzleIndex, smudge):
    global oldReflectionIndicesVertical
    possibleReflectionValues = dict()
    possibleReflectionValues[0] = -1

    prevColumn = getColumn(puzzleMap, 0)
    for i in range(1,len(puzzleMap[0])):
        smudgeExists = False
        currColumn = getColumn(puzzleMap, i)
        piecesEquivalent = currColumn == prevColumn
        if (not piecesEquivalent) and (not smudgeExists and smudge) and compareWithSmudge(currColumn, prevColumn):
            piecesEquivalent = True
            smudgeExists = True

        if piecesEquivalent:
            firstIndex = i - 1
            secondIndex = i

            if (puzzleIndex in oldReflectionIndicesVertical and oldReflectionIndicesVertical[puzzleIndex] == firstIndex):
                continue

            distanceFromStart = firstIndex - 0
            distanceFromEnd = len(puzzleMap[0]) - secondIndex - 1
            
            numberOfLinesToCheck = min(distanceFromStart, distanceFromEnd)
            matchingLines = 0

            for i in range(1,numberOfLinesToCheck+1):
                firstColumn = getColumn(puzzleMap, firstIndex - i)
                secondColumn = getColumn(puzzleMap, secondIndex + i)
                if (firstColumn == secondColumn):
                    matchingLines += 1
                elif (not smudgeExists and smudge) and compareWithSmudge(firstColumn,secondColumn):
                    matchingLines += 1
                    smudgeExists = True
            
            if matchingLines == numberOfLinesToCheck:
                possibleReflectionValues[firstIndex + 1] = firstIndex
        else:
            prevColumn = currColumn

    maxReflectionValue = max(possibleReflectionValues.keys())
    if (puzzleIndex not in oldReflectionIndicesVertical):
        oldReflectionIndicesVertical[puzzleIndex] = possibleReflectionValues[maxReflectionValue]

    return maxReflectionValue

def findReflection(puzzleMap, puzzleIndex, secondIteration):
    returnSum = 0
    returnSum += findHorizontalReflection(puzzleMap, puzzleIndex, secondIteration)
    returnSum += findVerticalReflection(puzzleMap, puzzleIndex, secondIteration)
    return returnSum

def findSumOfReflections():
    totalSum = 0
    secondIteration = False
    for i in range(2):
        with open('./day13input.txt', 'r') as file:
            puzzleMap = []
            puzzleNumber = 0

            for line in file:
                if line != '\n':
                    characters = []
                    for char in line:
                        if (char != '\n'):
                            characters.append(char)
                    puzzleMap.append(characters)
                else:
                    totalSum += findReflection(puzzleMap, puzzleNumber, secondIteration)
                    puzzleNumber += 1
                    puzzleMap = []

            totalSum += findReflection(puzzleMap, puzzleNumber, secondIteration)

        if not (secondIteration):
            totalSum = 0
            secondIteration = True
        
    print(totalSum)

if __name__ == "__main__":
    findSumOfReflections()