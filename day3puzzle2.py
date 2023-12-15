totalSum = 0
line1 = dict()
line2 = dict()
# Keeps track of number of parts associated with a gear
prevCharacterIndices = dict()

def parseLine(line):
    parsedLine = dict()
    for index in range(len(line)):
        if (line[index].isdigit()):
            parsedLine[index] = line[index]
        elif (line[index] != '.' and ord(line[index]) != 10):
            parsedLine[index] = '*'
    return parsedLine

def parseNumberToLeft(index, currentLine):
    line = line2 if currentLine else line1

    finalNumberString = line[index]
    del line[index]

    currIndex = index
    while (currIndex - 1 in line and line[currIndex - 1] != '*'):
        finalNumberString = line[currIndex - 1] + finalNumberString
        del line[currIndex - 1]
        currIndex -= 1
    return finalNumberString
        

def parseNumberToRight(index, currentLine):
    line = line2 if currentLine else line1

    finalNumberString = line[index]
    del line[index]

    currIndex = index
    while (currIndex + 1 in line and line[currIndex + 1] != '*'):
        finalNumberString = finalNumberString + line[currIndex + 1]
        del line[currIndex + 1]
        currIndex += 1
    return finalNumberString

def parseNumber(index, currentLine):
    line = line2 if currentLine else line1

    leftSide = ""
    rightSide = ""
    middle = ""
    adjacentValues = []
    
    if (index - 1 in line and line[index - 1] != "*"):
        leftSide = parseNumberToLeft(index-1, currentLine)
    if (index + 1 in line and line[index + 1] != "*"):
        rightSide = parseNumberToRight(index+1, currentLine)
    if (index in line and line[index] != '*'):
        middle = line[index]
        del line[index]
    
    if (middle != ""):
        adjacentValues.append(int(leftSide + middle + rightSide))
    else:
        leftSide = int(leftSide) if leftSide != '' else 0
        rightSide = int(rightSide) if rightSide != '' else 0
        if (leftSide > 0):
            adjacentValues.append(leftSide)
        if (rightSide > 0):
            adjacentValues.append(rightSide)

    return adjacentValues

def findValidNumbers():
    global totalSum
    global prevCharacterIndices
    characterIndices = dict()
    for key, value in line2.items():
        if value == '*':
            characterIndices[key] = []
    for index in characterIndices.keys():
        # Find numbers adjacent to character on same line
        characterIndices[index] += parseNumber(index, True)
        # Find numbers adjacent to character on line above
        characterIndices[index] += parseNumber(index, False)
    for index in prevCharacterIndices.keys():
        # Find numbers in current line adjacent to symbol on line above
        prevCharacterIndices[index] += parseNumber(index, True)
    
    # PrevCharacterIndices are about to be removed, so check to see if any have only two values
    for key, value in prevCharacterIndices.items():
        if len(value) == 2:
            totalSum += (value[0] * value[1])

    prevCharacterIndices = characterIndices


def findTotalSum():
    global line1
    global line2
    with open('./day3input.txt', 'r') as file:
        for line in file:
            line2 = parseLine(line)
            findValidNumbers()
            line1 = line2
        

if __name__ == "__main__":
    findTotalSum()
    print(totalSum)