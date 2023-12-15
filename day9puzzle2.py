historyValues = []

def parseFile():
    global historyValues
    with open('./day9input.txt', 'r') as file:
        for line in file:
            historyValues.append(line.split())

def findPrevValue(history):
    differences = []
    for i in range(1,len(history)):
        currDifference = int(history[i]) - int(history[i-1])
        differences.append(currDifference)
    if (len(set(differences)) == 1):
        nextIncrement = differences[0]
    else:
        nextIncrement = findPrevValue(differences)
    
    return int(history[0]) - nextIncrement

if __name__ == "__main__":
    parseFile()
    totalSum = 0
    for history in historyValues:
        totalSum += findPrevValue(history)
    print(totalSum)
