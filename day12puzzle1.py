import math


def getGroups(line):
    groupList = []
    group = ""
    for char in line:
        if (char != '.'):
            group += char
        else:
            if (group != ""):
                groupList.append(group)
            group = ""
    if (group != ""):
        groupList.append(group)
    return groupList

def findVariations(group, groupNumbers):
    numerator = math.factorial(sum(groupNumbers) + )

def findTotalVariations():
    totalVariations = 0
    with open('./day12inputtest.txt', 'r') as file:
        for line in file:
            damagedPipes = line.split()
            groups = getGroups(damagedPipes[0])
            groupNumbers = [int(item) for item in damagedPipes[1].split(',')]
            for group in groups:
                if group[0] == '#' and len(group) in groupNumbers:
                    groups.remove(group)
                    groupNumbers.remove(len(group))
            totalVariations += findVariations(groups, groupNumbers)
            print(totalVariations)
            break

if __name__ == "__main__":
    findTotalVariations()