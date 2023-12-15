totalSum = 0

spelledOutNumbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

def parseNumbers(line):
    global totalSum
    possibleNumbers = dict();
    firstDigitIndex = None
    secondDigitIndex = None
    totalLineLength = len(line) - 1

    # Find indexes for first and last number and add to possibleNumbers dictionary
    while (firstDigitIndex == None and secondDigitIndex == None):
        for index in range(len(line)):
            if (line[index].isdigit() and firstDigitIndex == None):
                firstDigitIndex = index
                possibleNumbers[firstDigitIndex] = int(line[firstDigitIndex])
            if (line[totalLineLength - index].isdigit() and secondDigitIndex == None):
                secondDigitIndex = totalLineLength - index
                possibleNumbers[secondDigitIndex] = int(line[secondDigitIndex])
    
    for index in range(9):
        if (spelledOutNumbers[index] in line):
            substringIndex = line.find(spelledOutNumbers[index], 0)
            while (substringIndex != -1):
                possibleNumbers[substringIndex] = index + 1
                substringIndex = line.find(spelledOutNumbers[index], substringIndex + 1)
    
    firstNumber = str(possibleNumbers[min(possibleNumbers)])
    secondNumber = str(possibleNumbers[max(possibleNumbers)])
    
    calibrationValue = int(firstNumber + secondNumber);
    print(calibrationValue)
    totalSum += calibrationValue

def iterateThroughFile():
    with open('./day1input.txt', 'r') as file:
        for line in file:
            parseNumbers(line)

if __name__ == "__main__":   
    iterateThroughFile()
    print(totalSum)