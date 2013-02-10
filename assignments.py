class AsgnHandler(object):
    def __init__(self, bld, vlgr):
        self.bld = bld
        self.vlgr = vlgr
    def assign(self, villager, building):
        """
        Adds the villager to asgns under that building name
        """
        if self.bld.built[str(building)].assignments < self.bld.built[str(building)].slots:
            self.bld.built[str(building)].assignments += 1
            self.bld.asgns[str(building)].add(villager)
            print villager, "assigned to", building
        else:
            print "That location is full"
    def auto_assign(self):
        for building in self.bld.built.itervalues():
            for person in self.vlgr.vlgrList.itervalues():
                if building.assignments < building.slots:
                    if person.sector == building.sector:
                        if person.workplace == '':
                            self.assign(person, building)
                            person.workplace = str(building)
        print self.bld.asgns
    def get_workplaces(self):
        for person in self.vlgr.vlgrList.itervalues():
            print person.workplace
