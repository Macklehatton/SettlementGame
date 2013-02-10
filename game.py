from storage import *
from villagers import *
from buildings import *
from production import *
from assignments import *


def main():
    pass

if __name__ == '__main__':
    main()

strg = Storage()
bld = BldHandler(strg)
vlgr = VlgrHandler()
asgn = AsgnHandler(bld, vlgr)
prod = Production(bld, vlgr, strg)


class DayInput(object):
    def __init__(self):
        startingPop = 20
        while startingPop > 0:
            vlgr.generate_adult()
            startingPop -= 1
        self.day = 1
    def pass_day(self):
        pass
    def input(self):
        running = True
        while running == True:
            print "Commands: build, assign, auto, end, help, exit"
            command = raw_input('>>')
            if command == 'build':
                bld.multi_construct(raw_input("What kind?\n"), int(raw_input("How many?\n")))
            elif command == 'oldbuild':
                bld.construct(raw_input("What kind?\n"))
            elif command == 'assign':
                asgn.assign(raw_input("Assign who?\n"),raw_input("Assign to where?\n"))
            elif command == 'auto':
                asgn.auto_assign()
            elif command == 'end':
                self.day += 1
                prod.calc_production()
                print prod.calc_consumption()
            elif command == 'help':
                print "help info"
            elif command == 'exit':
                running = False
            else:
                print "Unknown command"




day = DayInput()

vlgr.display_all()

day.input()

print bld.built
print bld.asgns
#asgn.get_workplaces()