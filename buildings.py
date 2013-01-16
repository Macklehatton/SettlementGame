# Buildings

class Buildings(object):
    """
    Class for handling buildings. Constructs them, contains a dictionary
    of all constructed buildings, a method for displaying them
    """
    def __init__(self):
        self.ID = 1
        self.built = {}
    def construct(self, kind, quality):
        """
        Constructor for buidlings
        """
        if kind in buildingList:
            self.built[kind + " " + str(self.ID)] = buildingList[kind].copy()
            self.built[kind + " " + str(self.ID)]["quality"] = quality
            self.ID += 1
        else:
            print "That building is not in the list of available buidlings."
    def displayBuilt(self):
        """
        Prints the dictionary of constructed buildings-- built-- in a
        readable format
        """
        for key in sorted(self.built):
            print key
            for e in self.built[key]:
                print e + ":", self.built[key][e]
            print ""



buildingList = {
    #List of all buildings that can be built
    "farm" : {"quality": 0, "slots" : 8},
    "logging camp" : {"quality": 1, "slots" : 12},
    "quarry": {"quality": 1, "slots" : 20},
    "trade post": {"quality": 1, "slots" : 5}
    }


# Instance of Buidlings
buildings = Buildings()