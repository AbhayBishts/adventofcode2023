totalSum = 0
line1 = dict()
line2 = dict()
prevCharacterIndices = []

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
    finalSum = 0
    
    if (index - 1 in line and line[index - 1] != "*"):
        leftSide = parseNumberToLeft(index-1, currentLine)
    if (index + 1 in line and line[index + 1] != "*"):
        rightSide = parseNumberToRight(index+1, currentLine)
    if (index in line and line[index] != '*'):
        middle = line[index]
        del line[index]
    
    if (middle != ""):
        finalSum = int(leftSide + middle + rightSide)
    else:
        leftSide = int(leftSide) if leftSide != '' else 0
        rightSide = int(rightSide) if rightSide != '' else 0
        finalSum = leftSide + rightSide

    if (finalSum > 0):
        print(finalSum)
    return finalSum

def findValidNumbers():
    global totalSum
    global prevCharacterIndices
    characterIndices = []
    for key, value in line2.items():
        if value == '*':
            characterIndices.append(key)
    for index in characterIndices:
        # Find numbers adjacent to character on same line
        totalSum += parseNumber(index, True)
        # Find numbers adjacent to character on line above
        totalSum += parseNumber(index, False)
    for index in prevCharacterIndices:
        # Find numbers in current line adjacent to symbol on line above
        totalSum += parseNumber(index, True)
    
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