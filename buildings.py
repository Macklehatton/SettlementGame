# Buildings

from villagers import *

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
    def getSkill(self, building):
         return buildingList[building]["skill"]
    def getOuput(self, building):
        return buildingList[building]["output"]






buildingList = {
    #List of all buildings that can be built
    "farm" : {
    "construction" : {"materials" : {"lumber" : 20}, "shifts" : 30},
    "output" : "food",
    "quality": 1,
    "skill" : "farm",
    "slots" : 8,
    "assignments" : 0},


    "logging camp" : {
    "construction" : {"materials" : {}, "shifts" : 15},
    "output" : "lumber",
    "quality": 1,
    "skill" : "lumberjack",
    "slots" : 12,
    "assignments" : 0},

    "quarry": {
    "construction" : {"materials" : {"lumber" : 40}, "shifts" : 30},
    "output" : "stone",
    "quality": 1,
    "skill" : "mine",
    "slots" : 20,
    "assignments" : 0},

    "trade post": {
    "construction" : {"materials" : {"lumber" : 30, "stone" : 10}, "shifts" : 30},
    "quality": 1,
    "output" : "money",
    "skill" : "trade",
    "slots" : 5,
    "assignments" : 0}
    }

bld = Buildings()


# add time component for building that varies by who is building it
# time: 8 would be 8 shifts of work. Consider adding a minimum