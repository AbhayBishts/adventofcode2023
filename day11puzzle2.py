galaxies = []
emptyRows = []
emptyColumns = []

def findEmptyRowsColumns(nonEmptyArray, total):
    emptyRowColumn = []
    for i in range(total):
        if i not in nonEmptyArray:
            emptyRowColumn.append(i)
    return emptyRowColumn

def parseFile():
    global galaxies
    global emptyRows
    global emptyColumns
    totalRows = set()
    totalColumns = set()
    with open('day11input.txt', 'r') as file:
        rowNumber = 0
        for line in file:
            columnNumber = 0
            for char in line:
                if (char == '#'):
                    galaxies.append((rowNumber,columnNumber))
                    totalRows.add(rowNumber)
                    totalColumns.add(columnNumber)
                columnNumber += 1
            rowNumber += 1
    
    emptyRows = findEmptyRowsColumns(totalRows, rowNumber)
    emptyColumns = findEmptyRowsColumns(totalColumns, columnNumber)

def expandedGalaxyLength(currentVal, targetVal, emptyArray):
    additionalLength = 0
    for i in range(min(currentVal, targetVal), max(currentVal,targetVal)):
        if i in emptyArray:
            additionalLength += 999999
    return additionalLength

def findPath(currentNode, targetNode):
    currRow, currCol = currentNode
    targRow, targCol = targetNode

    pathLength = abs(currRow-targRow) + abs(currCol - targCol)

    pathLength += expandedGalaxyLength(currRow, targRow, emptyRows)

    pathLength += expandedGalaxyLength(currCol, targCol, emptyColumns)

    return pathLength

def findShortestPaths():
    totalLength = 0
    for i in range(len(galaxies)-1):
        currentNode = galaxies[i]
        for j in range(i+1,len(galaxies)):
            targetNode = galaxies[j]
            totalLength += findPath(currentNode, targetNode)
    print(totalLength)

if __name__ == '__main__':
    parseFile()
    findShortestPaths()