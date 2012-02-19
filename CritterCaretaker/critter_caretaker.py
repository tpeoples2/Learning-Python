# Critter Caretaker

class Critter(object):
    """A virtual pet."""
    
    def __init__(self, name, hunger = 0, boredom = 0):
        self.name = name
        self.hunger = hunger
        self.boredom = boredom
    
    def __pass_time(self):
        self.hunger += 1
        self.boredom += 1

    @property
    def mood(self):
        unhappiness = self.hunger + self.boredom
        if unhappiness < 5:
            m = "happy"
        elif 5 <= unhappiness <= 10:
            m = "okay"
        elif 10 <= unhappiness <= 15:
            m = "pissed off"
        else:
            m = "enraged beyond control"
        return m

    def talk(self):
        print("I'm " + self.name + " and I feel " + self.mood + " now.\n")
        self.__pass_time()

    def eat(self, food = 4):
        print("That was some damn good food.")
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time()

    def play(self, fun = 4):
        print("Running around like a fool!")
        self.boredom -= fun
        if self.boredom < 0:
            boredom = 0
        self.__pass_time()

def main():
    crit_name = raw_input("What do you want to name your critter?: ")
    crit = Critter(crit_name)
    
    choice = None
    while choice != 0:
        print(
        """
        Critter Caretaker

        0 - quit
        1 - listen to your critter
        2 - feed your critter
        3 - play with your critter
        """)

        choice = int(raw_input("Choice: "))

        if choice == 0:
            print("Good-bye.")
        elif choice == 1:
            crit.talk()
        elif choice == 2:
            crit.eat()
        elif choice == 3:
            crit.play()
        else:
            print("\nUnknown choice, try again.")

main()

