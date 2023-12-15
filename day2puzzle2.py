totalPower = 0

def gamePowerSum():
    global totalPower
    with open('./day2input.txt', 'r') as file:
        for line in file:
            gameResults = line.split(':')[1].split(';')
            maxColorCount = {"green":0, "red":0, "blue":0}
            for result in gameResults:
                colorList = result.split(',')
                for color in colorList:
                    countAndColor = color.split()
                    count = int(countAndColor[0])
                    color = countAndColor[1]
                    maxColorCount[color] = max(count, maxColorCount[color])
            power = 1
            for count in maxColorCount.values():
                power *= count
            totalPower += power
            


if __name__ == "__main__":
    gamePowerSum()
    print(totalPower)