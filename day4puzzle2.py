totalCardCount = dict()

def incrementCardCount(index):
    global totalCardCount
    if (index in totalCardCount):
        totalCardCount[index] += 1
    else:
        totalCardCount[index] = 1

def calculateCardPoints(line, cardIndex):
    incrementCardCount(cardIndex)

    numberOfMatches = 0

    numbersOnly = line.split(':')[1].split('|')
    winningNumbers = numbersOnly[0].split()
    currentNumbers = numbersOnly[1].split()
    for number in currentNumbers:
        if (number in winningNumbers):
            numberOfMatches += 1
    
    for x in range(totalCardCount[cardIndex]):
        for index in range(cardIndex+1,cardIndex+1+numberOfMatches):
            incrementCardCount(index)


def findTotalPoints():
    with open('./day4input.txt', 'r') as file:
        cardNumber = 1
        for line in file:
            calculateCardPoints(line, cardNumber)
            cardNumber += 1
    
    totalCardCountNumber = 0

    for value in totalCardCount.values():
        totalCardCountNumber += value

    print(totalCardCountNumber)

if __name__ == "__main__":
    findTotalPoints()