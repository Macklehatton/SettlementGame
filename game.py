from villagers import *
from production import *
from buildings import *

def main():
    pass

main()



vlgr.create("Jed", {"farm": 8, "lumberjack" : 4, "fish" : 2, "carpentry" : 2})
vlgr.create("Noah", {"farm": 7, "lumberjack" : 3, "fish" : 3})



bld.construct("farm", 1)
bld.construct("farm", 1)
bld.construct("farm", 2)

vlgr.assign("Villager 1", "farm 1")



print bld.built

print vlgr.asgns

#print vlgr.vlgrLst[vlgr.asgns["farm 1 slot 1"]]["skills"]["farm"]

print production.calcProduction()


## function to pass the day