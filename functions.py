import json

def loadJson(jsonName):
    file = open(jsonName)
    dictonary = json.load(file)
    file.close
    return dictonary

def upgradeOre(upgrader, upgraders, ore):
    if upgraders[upgrader]["upgradeCounterLimit"] and ore["upgradeCounter"] > upgraders[upgrader]["upgradeCounterLimit"]:
        return ore
    if upgraders[upgrader]["Uselimit"]:
        if ore["usedUpgraders"].get(upgrader, False):
            if ore["usedUpgraders"][upgrader]["count"] > upgraders[upgrader]["Uselimit"]:
                return ore
            
    ore["upgradeCounter"] += upgraders[upgrader]["upgradeCounter"]

    ore = chooseUpgrade(upgrader, upgraders, ore)

    if upgrader in ore["usedUpgraders"]:
        ore["usedUpgraders"][upgrader]["count"] += 1
        
    else:
        tempDict = {upgrader:{
            "count": 1,
            "resettable": upgraders[upgrader]["resettable"]
        }}
        ore["usedUpgraders"].update(tempDict)

    return ore

def basicUpgrade(upgrader, upgraders, ore):
    print('a')
    print(upgrader)
    ore["Value"] += upgraders[upgrader]["additive"]
    ore["Value"] *= upgraders[upgrader]["multiplicative"]
    return ore

def resetOre(upgrader, upgraders, ore):
    for upgrade in ore["usedUpgraders"]:
        if ore["usedUpgraders"][upgrade]["resettable"] == True:
            ore["usedUpgraders"][upgrade]["count"] == 0

    return basicUpgrade(upgrader, upgraders, ore)

def rangeUpgrader(upgrader, upgraders, ore):
    length = len(upgraders[upgrader]["limits"])
    for x in range(0, length):
        if upgraders[upgrader]["limits"][x] == "infinite" or ore["Value"] < upgraders[upgrader]["limits"][x]:
            ore["Value"] += upgraders[upgrader]["additive"][x]
            ore["Value"] *= upgraders[upgrader]["multiplicative"][x]
            return ore


def processOre(furnace, furnaces, ore):
    ore["Value"] += furnaces[furnace]["additive"]
    ore["Value"] *= furnaces[furnace]["multiplicative"]
    return ore

def chooseUpgrade(upgrader, upgraders, ore):
    type = upgraders[upgrader]["type"]
    match type:
        case "basic":
            return basicUpgrade(upgrader, upgraders, ore)
        case "ranges":
            return rangeUpgrader(upgrader, upgraders, ore)
        case "resetter":
            return resetOre(upgrader, upgraders, ore)
        case "especial":
            code = compile(upgraders[upgrader]["code"], "something", "exec")
            exec(code)
            print(ore['Value'])
            return ore
