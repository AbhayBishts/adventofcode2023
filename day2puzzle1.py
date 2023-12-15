totalIDSum = 0
colorTotalCount = {"red":12, "green":13, "blue":14}

def gameIDSum():
    global totalIDSum
    with open('./day2input.txt', 'r') as file:
        for line in file:
            gameNumberAndResults = line.split(':')
            gameNumber = int(gameNumberAndResults[0].split()[1])
            gameResults = gameNumberAndResults[1].split(';')
            totalValidSubgames = 0
            for result in gameResults:
                colorList = result.split(',')
                totalValidColors = 0
                for color in colorList:
                    countAndColor = color.split()
                    count = int(countAndColor[0])
                    color = countAndColor[1]
                    if (count <= colorTotalCount[color]):
                        totalValidColors += 1
                if (totalValidColors == len(colorList)):
                    totalValidSubgames += 1
            if (totalValidSubgames == len(gameResults)):
                totalIDSum += gameNumber


if __name__ == "__main__":
    gameIDSum()
    print(totalIDSum)