import json

def loadJson(jsonName):
    file = open(jsonName)
    dictonary = json.load(file)
    file.close
    return dictonary

def upgradeOre(upgrader, upgraders, oreWorth):
    oreWorth += upgraders[upgrader]["additive"]
    oreWorth *= upgraders[upgrader]["multiplicative"]
    return oreWorth

def processOre(furnace, furnaces, oreWorth):
    oreWorth += furnaces[furnace]["additive"]
    oreWorth *= furnaces[furnace]["multiplicative"]
    return oreWorth