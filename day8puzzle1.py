from gettext import npgettext
import numpy as np

directions = None
nodeMapping = dict()

def parseInput():
    global directions
    global nodeMapping
    global firstNode
    with open('./day8input.txt', 'r') as file:
        nodeMappingValues = False
        for line in file:
            if nodeMappingValues:
                translation_table = str.maketrans('=,()', '    ')
                values = line.translate(translation_table).split()
                if len(values) > 0:
                    nodeMapping[values[0]] = [values[1],values[2]]
            else:
                directions = line.strip()
                nodeMappingValues = True

def findNumberOfSteps():
    currentNodes = [value for value in nodeMapping.keys() if value.endswith('A')]
    numberOfSteps = 0
    endingSteps = set()

    while (len(currentNodes) > 0):
        for char in directions:
            if (char == 'L'):
                direction = 0
            elif (char == 'R'):
                direction = 1
            for i in range(len(currentNodes)):
                currentNodes[i] = nodeMapping[currentNodes[i]][direction]
            numberOfSteps += 1
            finishedNodeIndices = [index for index, value in enumerate(currentNodes) if value.endswith('Z')]
            if (len(finishedNodeIndices) > 0):
                endingSteps.add(numberOfSteps)
            for index in finishedNodeIndices:
                currentNodes.pop(index)

    print(endingSteps)
    print(np.lcm.reduce(list(endingSteps)))

if __name__ == "__main__":
   parseInput()
   findNumberOfSteps()