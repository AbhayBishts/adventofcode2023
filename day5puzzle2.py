import multiprocessing
import sys

seedList = []
seedToSoilMaps = []
soilToFertilizerMaps = []
fertilizerToWaterMaps = []
waterToLightMaps = []
lightToTempMaps = []
tempToHumidityMaps = []
humidityToLocationMap = []

def parseFile():
    global seedList
    global seedToSoilMaps
    global soilToFertilizerMaps
    global waterToLightMaps
    global lightToTempMaps
    global tempToHumidityMaps
    global humidityToLocationMap
    with open('./day5input.txt', 'r') as file:
        lines = file.readlines()
        seedList = lines[0].split(':')[1].split()
        currList = None
        for index in range(2, len(lines)):
            if ('seed-to-soil' in lines[index]):
                currList = seedToSoilMaps
            elif ('soil-to-fertilizer' in lines[index]):
                currList = soilToFertilizerMaps
            elif ('fertilizer-to-water' in lines[index]):
                currList = fertilizerToWaterMaps
            elif ('water-to-light' in lines[index]):
                currList = waterToLightMaps
            elif ('light-to-temperature' in lines[index]):
                currList = lightToTempMaps
            elif ('temperature-to-humidity' in lines[index]):
                currList = tempToHumidityMaps
            elif ('humidity-to-location' in lines[index]):
                currList = humidityToLocationMap
            else:
                numberList = lines[index].split()
                if (len(numberList) > 0):
                    currList += [numberList]

parseFile()

def findMaxLocationValue():
    maxLocationValue = 0
    for values in humidityToLocationMap:
        maxLocationValue = max(maxLocationValue, int(values[0]) + int(values[2]))
    return maxLocationValue

def correspondingValueReverse(dest, mapList):
    dest = int(dest)

    sourceNumber = dest
    for values in mapList:
        destValue = int(values[0])
        sourceValue = int(values[1])
        rangeValue = int(values[2])
        if (dest in range(destValue, destValue + rangeValue)):
            difference = dest - destValue
            sourceNumber = sourceValue + difference
    
    return sourceNumber

def seedExists(seed):
    for index in range(0, len(seedList), 2):
        seedStart = int(seedList[index])
        seedRange = int(seedList[index+1])
        if (seed in range(seedStart, seedStart + seedRange)):
            return True
    return False

def createIncrementedIndices(processes):
    stepSize = int(maxLocationValue // processes)
    argumentList = []
    for i in range(processes):
        argumentList.append(stepSize * i)
    return argumentList
    
def findSmallestLocation():
    maxLocationValue = findMaxLocationValue()
    for location in range(maxLocationValue):
        if (location % 100000 == 0):
            print(f'Location: {location}')
        humidity = correspondingValueReverse(location, humidityToLocationMap)
        temp = correspondingValueReverse(humidity, tempToHumidityMaps)
        light = correspondingValueReverse(temp, lightToTempMaps)
        water = correspondingValueReverse(light, waterToLightMaps)
        fertilizer = correspondingValueReverse(water, fertilizerToWaterMaps)
        soil = correspondingValueReverse(fertilizer, soilToFertilizerMaps);
        seed = correspondingValueReverse(soil, seedToSoilMaps)
        if (seedExists(seed)):
            print(location)
            break
    

if __name__ == "__main__":
    findSmallestLocation()