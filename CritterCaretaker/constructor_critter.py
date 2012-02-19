# Attribute Critter

class Critter(object):
    """A virtual pet."""
    total = 0

    @staticmethod
    def status():
        print("The total number of critters is " + str(Critter.total))

    def __init__(self, name):
        print("A new critter has been born!")
        self.name = name
        Critter.total += 1

    def __str__(self):
        rep = "Critter object\n"
        rep += "name: " + self.name + "\n"
        return rep

    def talk(self):
        print("\nHi, I'm " + self.name + "\n")

# main
print("Accessing the class attribute Critter.total: " + str(Critter.total))

crit1 = Critter("Poochie")
crit1.talk()
crit2 = Critter("Randoplh")
crit2.talk()
crit3 = Critter("Joey")

print("Printing crit1:")
print(crit1)

print("Printing crit2:")
print(crit2)

print("Directly accessing crit1.name: " + crit1.name)

Critter.status()
