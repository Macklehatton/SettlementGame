# Production, consumption

class Production(object):
    def __init__(self, bld, vlgr, strg):
        self.bld = bld
        self.vlgr = vlgr
        self.strg = strg
        self.ration = 1
    def calc_production(self):
        for building in self.bld.asgns:
            for villager in self.bld.asgns[building]:
                self.strg.storage[self.bld.built[building].output] += 5 + self.vlgr.vlgrList[str(villager)].skills[self.bld.built[building].skill]
    def calc_consumption(self):
        self.strg.storage["food"] -= self.vlgr.population * self.ration
        return self.strg.storage


