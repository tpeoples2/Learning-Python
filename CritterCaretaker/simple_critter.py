# Simple Critter

class Critter(object):
    """A virtual pet."""
    def talk(self):
        print("Hi, I'm an instance of class Critter.")

# main
crit = Critter()
crit.talk()

raw_input("\n\nPress the enter key to exit.")

