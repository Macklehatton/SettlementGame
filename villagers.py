#Villagers

## Actions: Assign, build

from buildings import *

class VillagerHandler(object):
    """
    Villager constructor
    """
    def __init__(self):
        """
        ID: Used so villagers have their own unique number
        vlgrLst: Dictionary for storing all the villagers
        """
        self.ID = 1
        self.vlgrLst = {}
        self.asgns = {}

    def create(self, name, skills):
        """
        Adds an entry to vlgrLst with a unique ID

        name: name of the villager (not the ID used in the villagers key)
        skills: should be dictionary listing all the skills the villager will
        have
        """
        self.vlgrLst["Villager " + str(self.ID)] = {"name" : name, "skills" : skills}
        self.ID += 1

    def assign(self, villager, building):
        """
        Adds the villager to the asgns for that building
        """
        if bld.built[building]["assignments"] < bld.built[building]["slots"]:
            bld.built[building]["assignments"] += 1
            self.asgns[building] = {"slot " + str(bld.built[building]["assignments"]) : villager}
            print villager, "assigned to", building
        else:
            print "That location is full"

    def getVlgrSkill(self, villager, skill):
        """
        Given the ID of the villager and the skill you want to find,
        returns the villagers value of that skill
        If the villager does not have that skill returns 0
        """
        if skill in vlgr.vlgrLst[villager]["skills"]:
            return vlgr.vlgrLst[villager]["skills"][skill]
        else:
            return 0
    def getId(self, name):
        for key in self.vlgrLst.iterkeys():
            if self.vlgrLst[str(key)]["name"] == name:
                return key
        else:
            raise RuntimeError("Name not found")

vlgr = VillagerHandler()



# Finish assignments
# They still allow one villager to be assigned to two locaitons
#
# getAsgns which displays asgns in a readable format
#
# Method to get the population, for consumption
#
# Create a method for Villagers, get by name, which returns the villager ID
# given the villager's name
#
#
# Randomly generate a villager
#
# Villager backgrounds
#
# Military personell (use the same system, any barriers are social),
# combat skills are a separate list
#
# Children
#
