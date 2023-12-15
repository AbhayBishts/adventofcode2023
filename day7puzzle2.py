pointsToHands = dict()
handBid = dict()

def parseInput():
    global handPoints
    global handBid
    with open('./day7input.txt', 'r') as file:
        for line in file:
            values = line.split()
            hand = values[0]
            bid = values[1]
            handBid[hand] = bid

def cardDictionary(hand):
    cardDict = dict()
    for card in hand:
        if (card not in cardDict):
            cardDict[card] = 1
        else:
            cardDict[card] += 1
    if ('J' in cardDict):
        jCount = cardDict['J']
        del cardDict['J']
        if (len(cardDict) > 0):
            highestFreqCard = max(cardDict, key=cardDict.get)
            cardDict[highestFreqCard] += jCount
        else:
            cardDict['J'] = jCount
    return cardDict

def pointsInHand(cardDict):
    uniqueCards = len(cardDict)
    points = 0
    if (uniqueCards == 1):
        points = 7 # Five of a kind 
    elif (uniqueCards == 2):
        if (4 in cardDict.values()):
            points = 6 # Four of a kind
        else:
            points = 5 # Full house (three of a kind and two of a kind)
    elif (uniqueCards == 3):
        if (3 in cardDict.values()):
            points = 4 # Three of a kind
        else:
            points = 3 # Two pairs
    elif (uniqueCards == 4):
        points = 2 # One pair
    elif (uniqueCards == 5):
        points = 1 # High card

    return points

def calculatePointValues():
    global pointsToHands
    for hand in handBid.keys():
        cardDict = cardDictionary(hand)
        points = pointsInHand(cardDict)

        if (points in pointsToHands):
            pointsToHands[points].append(hand)
        else:
            pointsToHands[points] = [hand]

def cardToPoints(card):
    cardPoints = {'A':14,'K':13,'Q':12,'J':1,'T':10}
    if card.isdigit():
        return int(card)
    else:
        return cardPoints[card]

def tiebreaker(hands, index):
    finalOrder = []
    cardPoints = dict()
    for hand in hands:
        points = cardToPoints(hand[index])
        if points in cardPoints:
            cardPoints[points].append(hand)
        else:
            cardPoints[points] = [hand]
    cardPointRankings = sorted(cardPoints.keys(), reverse=True)
    for cardPoint in cardPointRankings:
        if len(cardPoints[cardPoint]) == 1:
            finalOrder.append(cardPoints[cardPoint][0])
        else:
            finalOrder += tiebreaker(cardPoints[cardPoint],index+1)

    return finalOrder
        
def rankCards():
    pointRankings = sorted(pointsToHands.keys(), reverse=True)
    finalRankings = []
    for point in pointRankings:
        hands = pointsToHands[point]
        if len(hands) == 1:
            finalRankings.append(hands[0])
        else: # There is a tie
            finalRankings += tiebreaker(hands, 0)
    return finalRankings

def totalWinnings(ranking):
    multiplier = len(handBid)
    totalWinnings = 0
    for hand in ranking:
        totalWinnings += multiplier * int(handBid[hand])
        multiplier -= 1
    return totalWinnings

if __name__ == "__main__":
    parseInput()
    calculatePointValues()
    ranking = rankCards()
    print(ranking)
    winnings = totalWinnings(ranking)
    print(winnings)