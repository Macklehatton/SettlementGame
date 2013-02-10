class Villager(object):
    ID = 1
    def __init__(self, name, skills):
        self.name = name
        self.skills = skills
        self.vlgrID = "Villager " + str(Villager.ID)
        Villager.ID += 1
    def __repr__(self):
        return str(self.skills)


class VlgrHandler(object):
    def __init__(self):
        self.vlgrList = {}
    def create(self, name, skills):
        self.vlgrList[str(name)] = Villager(name, skills)
    def getSkill(self, villager, skill):
        if skill in self.vlgrList[villager].skills:
            return self.vlgrList[villager].skills
        else:
            return 0
    def getID(self, name):
        return self.vlgrList[name].vlgrID



VlgrHandler = VlgrHandler()

