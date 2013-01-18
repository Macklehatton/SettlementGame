#Storage, production, consumption

from villagers import *
from buildings import *

class Storage(object):
    def __init__(self, contents):
        self.contents = contents.copy()
    def getContents(self):
        return self.contents

class Consumption(object):
    def __init__(self, population, ration):
        self.population = population
        self.ration = ration
    def calcConsumption(self):
        consumption = self.population * self.ration
        storage.contents["food"] -= consumption

class Production(object):
    """
    Production per villager = 10 + (villager skill * building quality)
    """
    def __init__(self):
        pass
    def calcProduction(self):
        food = 0
        stone = 0
        lumber = 0
        for building in vlgr.asgns:
            prod = bld.getOutput(building)
            prod += vlgr.getVlgrSkill(vlgr.getId("Noah"), bld.getSkill(building[:-2]))
        return food, stone, lumber






production = Production()

resourceList = {
    "food" : 0,
    "wood" : 0,
    "stone" : 0,
    "money" : 0
    }


storage = Storage(resourceList.copy())

consumption = Consumption(30, 1)
consumption.calcConsumption()

print storage.getContents()

# Work out production based on villagers assigned to buildings
