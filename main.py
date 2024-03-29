import json
import functions

droppers = functions.loadJson("droppers.json")
furnaces = functions.loadJson("furnaces.json")
upgraders = functions.loadJson("upgraders.json")

usedDropper = "Basic Iron Mine"
dropperAmount = 1
usedUpgraders = ["special"]
usedFurnace = "Basic Furnace"
ore = {"Value": droppers[usedDropper]["value"],
       "dropRate": droppers[usedDropper]["drop rate"],
       "upgradeCounter": droppers[usedDropper]["upgradeCounter"],
       "usedUpgraders": {}}
ore["Value"] = 100

for upgrader in usedUpgraders:
    oreWorth = functions.upgradeOre(upgrader, upgraders, ore)

ore = functions.processOre(usedFurnace, furnaces, ore)
print(ore)