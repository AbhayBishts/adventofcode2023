startPosition = None
pipes = dict()
iteratedPositions = set()

def parseFile():
    global startPosition
    global pipes
    with open('./day10input.txt', 'r') as file:
        row = 0
        for line in file:
            col = 0
            for char in line:
                if char == 'S':
                    startPosition = (row,col)
                if char != '.' and char != '\n':
                    pipes[(row,col)] = char
                col += 1
            row += 1

def validMove(type, move):
    invalidType = []
    if (move == 'right'):
        invalidType = ['|', 'J', '7']
    elif (move == 'left'):
        invalidType = ['|', 'F', 'L']
    elif (move == 'up'):
        invalidType = ['-', 'F', '7']
    elif (move == 'down'):
        invalidType = ['-', 'L', 'J']
    
    if type in invalidType:
        return False
    
    return True

def findNextLocation(currentPosition, type):
    row, col = currentPosition
    returnValue = None
    if (row,col+1) not in iteratedPositions and (row,col+1) in pipes and validMove(type, 'right'):
        if validMove(pipes[(row,col+1)], 'left'):
            returnValue = (row,col+1)
    elif (row,col-1) not in iteratedPositions and (row,col-1) in pipes and validMove(type, 'left'):
        if validMove(pipes[(row,col-1)], 'right'):
            returnValue = (row,col-1)
    elif (row-1,col) not in iteratedPositions and (row-1,col) in pipes and validMove(type, 'up'):
        if validMove(pipes[(row-1,col)], 'down'):
            returnValue = (row-1,col)
    elif (row+1,col) not in iteratedPositions and (row+1,col) in pipes and validMove(type, 'down'):
        if validMove(pipes[(row+1,col)], 'up'):
            returnValue = (row+1,col)

    return returnValue

def navigateRoute():
    global iteratedPositions
    iteratedPositions.add(startPosition)
    currentPosition = findNextLocation(startPosition, pipes[startPosition])
    iteratedPositions.add(currentPosition)
    numberOfSteps = 1
    while currentPosition != startPosition:
        currentPosition = findNextLocation(currentPosition, pipes[currentPosition])
        iteratedPositions.add(currentPosition)
        numberOfSteps += 1
        if (currentPosition == None):
            break
    print(numberOfSteps // 2)

if __name__ == "__main__":
    parseFile()
    navigateRoute()