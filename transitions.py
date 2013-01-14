#transitions

locations = {
    "kitchen" : ["A description of a kitchen", ["bedroom", "yard"]],
    "bedroom" : ["Bedroom description", ["kitchen"]],
    "yard" : ["Yard description", ["kitchen", "shed"]],
    "shed" : ["Shed description", ["yard"]]
}




class Transition(object):
    def __init__(self):
        self.currentLocation = start
    def describe(self):
        print "You are in the", self.currentLocation
        print locations[self.currentLocation][0]
        print "Go to:"
        for i in locations[self.currentLocation][1]:
            print i
    def goTo(self, location):
        if location == self.currentLocation:
            print "You are already in the", location
        elif location in locations[self.currentLocation][1]:
            print "You go to the", location
            self.currentLocation = location
            self.describe()
        else:
            print "You can't get there from here"







transition = Transition()

transition.goTo("shed")
transition.goTo("bedroom")