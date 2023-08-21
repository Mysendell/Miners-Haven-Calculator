import json

def loadJson(jsonName):
    file = open(jsonName)
    dictonary = json.load(file)
    file.close
    return dictonary

def upgradeOre(upgrader, upgraders, ore):
    if not upgraders[upgrader]["upgradeCounterLimit"] or ore["upgradeCounter"] < upgraders[upgrader]["upgradeCounterLimit"]:
        if not upgraders[upgrader]["Uselimit"] or ore["usedUpgraders"].get(upgrader, 0) < upgraders[upgrader]["Uselimit"]:

            upgradeType = chooseUpgrade(upgrader, upgraders)
            ore["Value"] = upgradeType(upgrader, upgraders, ore["Value"])

            ore["upgradeCounter"] += upgraders[upgrader]["upgradeCounter"]
            
            if upgrader not in ore["usedUpgraders"]:
                ore["usedUpgraders"][upgrader] = 1
            else:
                ore["usedUpgraders"][upgrader] += 1

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
