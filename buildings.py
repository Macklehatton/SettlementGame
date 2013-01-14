# Buildings

buildingList = ["farm", "logging camp", "quarry", "trade post"]

class Buildings(object):
    def __init__(self):
        self.ID = 1
    def building(self, kind, quality):
        self.kind = kind
        self.quality = quality
        self.slots = 2
        return [kind, quality]
    def construct(self, kind, quality):
        if kind in buildingList:
            built[kind + " " + str(self.ID)] = self.building(kind, quality)
            self.ID += 1

buildings = Buildings()

built = {}

buildings.construct("farm", 1)
buildings.construct("farm", 1)
buildings.construct("farm", 1)

print built['farm 1'.slots]

# farmID : [kind, quality, slots]

