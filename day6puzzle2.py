time = []
distance = []

distanceRate = 1

def parseFile():
    global time
    global distance
    with open('./day6input.txt', 'r') as file:
        timeValue = True
        for line in file:
            value = line.split(':')[1].split()
            value = int(''.join(map(str, value)))
            if timeValue:
                time = int(value)
            else:
                distance = int(value)
            timeValue = False

def waysToWin():
    winningRange = []
    leftBound = True
    for chargeTime in range(1,time):
        currDistance = (chargeTime * distanceRate) * (time - chargeTime)
        if (leftBound and currDistance > distance):
            winningRange.append(chargeTime)
            leftBound = False
        if ((not leftBound) and currDistance < distance):
            winningRange.append(chargeTime)
            break
    print(winningRange[1] - winningRange[0])

if __name__ == "__main__":
    parseFile()
    waysToWin()