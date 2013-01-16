#Villagers

## Actions: Assign, build

from buildings import *

class Villager(object):
    """
    Villager constructor
    """
    def __init__(self):
        self.ID = 1
        self.villagers = {}

    def create(self, name, skills):
        self.villagers[name + " " + ID] = {"name" : name, "skills" : skills}
        self.ID += 1
    def assign(self, villager, task):
        if buildings.slots >= 0:
            pass
            print self.name, "assigned to", task
        else:
            "That assignment if full becuase", "there's no room", "or that resource is unavailable"

