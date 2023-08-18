import json
import functions

droppers = functions.loadJson("droppers.json")
furnaces = functions.loadJson("furnaces.json")
upgraders = functions.loadJson("upgraders.json")


usedDropper = "Basic Iron Mine"
dropperAmount = 1
usedUpgraders = ["Fine-Point Upgrader", "Fine-Point Upgrader"]
usedFurnace = "Basic Furnace"
oreWorth = droppers[usedDropper]["value"]

for x in usedUpgraders:
    oreWorth = functions.upgradeOre(x, upgraders, oreWorth)

finalOreWorth = functions.processOre(usedFurnace, furnaces, oreWorth)
print(finalOreWorth)