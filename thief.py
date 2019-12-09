class Thief():

    def __init__(self):
        self.initiative = 7
        self.durability = 5
        self.attack = 5
        self.agility = 7

    def ability_discription(self):

        print("\n3-Thief")
        print(f" ---------------")
        print(f"| Initiative = {self.initiative}|")
        print(f"| Durability = {self.durability}|")
        print(f"| Attack     = {self.attack}|")
        print(f"| Agility    = {self.agility}|")
        print(f" ---------------")
        print(f"\nSpecial ability :-----------------------------------------------")
        print(f"|Critical hit. The thief has a 25% chance of doing double damage|\n"
              f"|every time the thief attacks.                                  |")
        print(f" ---------------------------------------------------------------")
