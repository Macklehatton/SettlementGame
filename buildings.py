import copy

class Building(object):
    def __init__(self, kind, bldID, quality, materials, shifts, output, sector, skill, slots, assignments):
        self.kind = kind
        self.bldID = bldID
        self.quality = quality
        self.materials = materials
        self.shifts = shifts
        self.output = output
        self.sector = sector
        self.skill = skill
        self.slots = slots
        self.assignments = assignments
    def __repr__(self):
        return self.kind + " " + str(self.bldID)


class BldHandler(object):
    """
    Stores building info, constructed buildings, and function for building them
    """
    def __init__(self, strg):
        self.strg = strg
        self.built = {}
        self.buildingList = {
            "farm" : Building("farm", 1, 1, {"lumber" : 20}, 30, "food", "agriculture", "farm", 8, 0),
            "logging camp" : Building("logging camp", 1, 1, {}, 10, "lumber", "logging", "lumberjack", 12, 0),
            "quarry" : Building("quarry", 1, 1, {"lumber" : 40}, 30, "stone", "mining", "mine", 20, 0),
            "trade post" : Building("trade post", 1, 1, {"lumber" : 30, "stone" : 10}, 30, "money", "trade", "trade", 30, 0),
        }
        self.asgns = {}
    def construct(self, kind):
        sufficient = True
        for material in self.buildingList[str(kind)].materials.iterkeys():
            if self.strg.storage[str(material)] >= self.buildingList[str(kind)].materials[str(material)]:
                pass
            else:
                sufficient = False
                print "Not enough pylons"
        if sufficient == True:
            self.built[kind + " " + str(self.buildingList[kind].bldID)] = copy.deepcopy(self.buildingList[kind])
            self.asgns[kind + " " + str(self.buildingList[kind].bldID)] = set()
            self.buildingList[kind].bldID += 1
    def multi_construct(self, kind, number):
        constructed = 0
        while constructed < number:
            self.construct(kind)
            constructed += 1
        print self.built



