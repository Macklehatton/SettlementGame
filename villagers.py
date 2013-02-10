from atomic import *
import random


atomic = Atomic()

class Villager(object):
    vlgrID = 1
    def __init__(self, name, age, sex, skills, sector):
        self.name = name
        self.age = age
        self.sex = sex
        self.skills = skills
        self.sector = sector
        self.vlgrID = "Villager " + str(Villager.vlgrID)
        self.workplace = ''
        Villager.vlgrID += 1
    def __repr__(self):
        return str(self.name)


class VlgrHandler(object):
    def __init__(self):
        self.vlgrList = {}
        self.population = 0
    def get_skill(self, villager, skill):
        if skill in self.vlgrList[villager].skills:
            return self.vlgrList[villager].skills
        else:
            return 0
    def get_ID(self, name):
        return self.vlgrList[name].vlgrID
    def rand_name(self, gender):
        if gender == 'male':
            atomic.atomize('italianmalenames')
            return atomic.name()
        else:
            atomic.atomize('italianfemalenames')
            return atomic.name()
    def generate_adult(self):
        sex = ''
        if random.random() >= 0.51:
            sex = 'male'
        else:
            sex = 'female'
        name = self.rand_name(sex).title()
        skills = {'farm' : 2}
        roll = random.random()
        if roll <= 0.90:
            #farmer background
            skills = {'farm' : 10, 'lumberjack' : 2}
            sector = 'agriculture'
        elif 0.90 < roll <= 0.95:
            #lumberjack
            skills['lumberjack'] = 10
            sector = 'logging'
        elif 0.95 < roll <= 0.99:
            #miner
            skills['mine'] = 10
            sector = 'mining'
        elif 0.99 < roll <= 100:
            #trader
            skills['trade'] = 10
            sector = 'trade'
        self.vlgrList[name] = Villager(name, random.randrange(16, 35), sex, skills, sector)
        self.population += 1
    def display_all(self):
        demographics_male = 0
        demographics_female = 0
        sectorAgro = 0
        sectorLog = 0
        sectorMine = 0
        sectorTrade = 0
        print "Villager List:/n"
        for person in self.vlgrList:
            print "Name: " + str(self.vlgrList[person].name)
            print "Age: " + str(self.vlgrList[person].age)
            print "Sex: " + str(self.vlgrList[person].sex)
            print "Skills: " + str(self.vlgrList[person].skills)
            print ''
            if self.vlgrList[person].sex == 'male':
                demographics_male += 1
            else:
                demographics_female += 1
            if self.vlgrList[person].sector == 'agriculture':
                sectorAgro += 1
            elif self.vlgrList[person].sector == 'logging':
                sectorLog += 1
            elif self.vlgrList[person].sector == 'mining':
                sectorMine += 1
            elif self.vlgrList[person].sector == 'trade':
                sectorTrade += 1
        print "Demographics:"
        print "Female: " + str(demographics_female)
        print "Male: " + str(demographics_male)
        print ""
        print "Sectors:"
        print "Agriculture: " + str(sectorAgro)
        print "Logging: " + str(sectorLog)
        print "Mining: " + str(sectorMine)
        print "Trade: " + str(sectorTrade)






