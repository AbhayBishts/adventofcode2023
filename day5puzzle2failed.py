from itertools import product
import multiprocessing
import sys
# import threading

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

def correspondingValue(seed, mapList):
    seed = int(seed)

    destNumber = seed
    for values in mapList:
        destValue = int(values[0])
        sourceValue = int(values[1])
        rangeValue = int(values[2])
        if (seed in range(sourceValue, sourceValue + rangeValue)):
            difference = seed - sourceValue
            destNumber = destValue + difference
    
    return destNumber

def findLocations(seedStart, seedRange):
    print(f'Starting thread, seedStart:{seedStart}, seedRange:{seedRange}')
    minLocation = sys.maxsize
    seedStart = int(seedStart)
    seedRange = int(seedRange)
    for seed in range(seedStart, seedStart + seedRange):
        soil = correspondingValue(seed, seedToSoilMaps)
        fertilizer = correspondingValue(soil, soilToFertilizerMaps)
        water = correspondingValue(fertilizer, fertilizerToWaterMaps)
        light = correspondingValue(water, waterToLightMaps)
        temp = correspondingValue(light, lightToTempMaps)
        humidity = correspondingValue(temp, tempToHumidityMaps)
        location = correspondingValue(humidity, humidityToLocationMap)
        minLocation = min(minLocation, location)
    
    return minLocation

def findSmallestLocation():
    # threads = []
    # for index in range(0, len(seedList), 2):
    #     threads.append(threading.Thread(target=findLocations, args=(seedList[index],seedList[index+1])))
    # for thread in threads:
    #     thread.start()
    # for thread in threads:
    #     thread.join()
    # print(min(locationList))

    numberOfProcesses = int(len(seedList)/2)
    argumentPairs = []
    for i in range(0, len(seedList), 2):
        argumentPairs.append((seedList[i], seedList[i + 1]))

    with multiprocessing.Pool(processes=numberOfProcesses) as pool:
        # Use the map function to apply the function to each parameter
        results = pool.starmap(findLocations, argumentPairs)

    print(min(results))

parseFile()

if __name__ == "__main__":
    findSmallestLocation()