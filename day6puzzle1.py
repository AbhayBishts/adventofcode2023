timeList = []
distanceList = []

distanceRate = 1

def parseFile():
    global timeList
    global distanceList
    with open('./day6input.txt', 'r') as file:
        time = True
        for line in file:
            values = line.split(':')[1].split()
            if (time):
                timeList = values
            else:
                distanceList = values
            time = False

def waysToWin(raceTime, recordDistance):
    raceTime = int(raceTime)
    recordDistance = int(recordDistance)
    waysToWin = 0
    for chargeTime in range(1,raceTime):
        distance = (chargeTime * distanceRate) * (raceTime - chargeTime)
        if (distance > recordDistance):
            waysToWin += 1
    return waysToWin

def totalWaysToWin():
    totalWaysToWin = 1
    for index in range(len(timeList)):
        raceTime = timeList[index]
        recordDistance = distanceList[index]
        totalWaysToWin *= waysToWin(raceTime, recordDistance)
    print(totalWaysToWin)

if __name__ == "__main__":
    parseFile()
    totalWaysToWin()