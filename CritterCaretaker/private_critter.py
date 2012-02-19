# Private Critter

class Critter(object):
    """A virtual pet."""
    total = 0

    @staticmethod
    def status():
        print("The current number of critters is " + str(Critter.total))

    def __init__(self, name, mood):
        print("A new critter has been born!")
        self.name = name    # public attribute
        self.__mood = mood  # private attribute
    
    def talk(self):
        print("I'm " + self.name)
        print("Right now I feel " + self.__mood + "\n")

    def __str__(self):
        string = "Name: " + self.name + "\n"
        string += "Mood: " + self.__mood
        return string

    def __private_method(self):
        print("This is a private method.")

    def public_method(self):
        print("This is a public method.")
        self.__private_method()

# main
crit = Critter(name = "Poochie", mood = "happy")
crit.talk()
print(crit)
crit.public_method()
