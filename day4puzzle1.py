totalPoints = 0

def calculateCardPoints(line):
    numbersOnly = line.split(':')[1].split('|')
    winningNumbers = numbersOnly[0].split()
    currentNumbers = numbersOnly[1].split()
    currentExponent = -1
    cardPoints = 0
    for number in currentNumbers:
        if (number in winningNumbers):
            currentExponent += 1
    if (currentExponent > -1):
        cardPoints = (2 ** currentExponent)
    return cardPoints
    

def findTotalPoints():
    global totalPoints
    with open('./day4input.txt', 'r') as file:
        for line in file:
            totalPoints += calculateCardPoints(line)

if __name__ == "__main__":
    findTotalPoints()
    print(totalPoints)