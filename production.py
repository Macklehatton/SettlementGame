#Storage, production, consumption

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


##class Production(object):
##    def __init__(self, assignments):

resourceList = {
    "food" : 0,
    "wood" : 0,
    "stone" : 0,
    "money" : 0
    }


storage = Storage(resourceList)

consumption = Consumption(30, 1)
consumption.calcConsumption()

print storage.getContents()

