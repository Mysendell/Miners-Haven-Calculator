import json

def loadJson(jsonName):
    file = open(jsonName)
    dictonary = json.load(file)
    file.close
    return dictonary

def upgradeOre(upgrader, upgraders, ore):
    if upgraders[upgrader]["upgradeCounterLimit"] == 0 or ore["upgradeCounter"] < upgraders[upgrader]["upgradeCounterLimit"]:
        if upgraders[upgrader]["Uselimit"] == 0 or dict.get(ore["usedUpgraders"][upgrader] < upgraders[upgrader]["Uselimit"])
            upgradeType = chooseUpgrade(upgrader, upgraders)
            ore["Value"] = upgradeType(upgrader, upgraders, ore["Value"])
            ore["upgradeCounter"] = upgraders[upgrader]["upgradeCounter"]
            
    return ore

def basicUpgrade(upgrader, upgraders, ore):
    ore += upgraders[upgrader]["additive"]
    ore *= upgraders[upgrader]["multiplicative"]
    return ore

def rangeUpgrader(upgrader, upgraders, ore):
    length = len(upgraders[upgrader]["limits"])
    for x in range(0, length):
        if upgraders[upgrader]["limits"][x] == "infinite" or ore < upgraders[upgrader]["limits"][x]:
            ore += upgraders[upgrader]["additive"][x]
            ore *= upgraders[upgrader]["multiplicative"][x]
            return ore


def processOre(furnace, furnaces, ore):
    ore["Value"] += furnaces[furnace]["additive"]
    ore["Value"] *= furnaces[furnace]["multiplicative"]
    return ore

def chooseUpgrade(upgrader, upgraders):
    type = upgraders[upgrader]["type"]
    match type:
        case "basic":
            return basicUpgrade
        case "ranges":
            return rangeUpgrader
