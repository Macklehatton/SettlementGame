#Villagers
from buildings import *

class Villager(object):
    def __init__(self, name, skills):
        self.name = name
        self.skills = skills

    def assign(self, task):
        if buildings.slots >= 0:
            pass
            print self.name, "assigned to", task
        else:
            "That assignment if full becuase", "there's no room", "or that resource is unavailable"

    def build(self):
        print "Building"


jed = Villager("Jed", {
    "farm" : 10,
    "fish" : 5,
    "build" : 2
    }
)


jed.assign("farm")