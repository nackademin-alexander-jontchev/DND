class Wizard:

    def __init__(self):
        self.initiative = 6
        self.durability = 4
        self.attack = 9
        self.agility = 5

    def ability_discription(self):
        print("\n2-Wizard")
        print(f" ---------------")
        print(f"| Initiative = {self.initiative}|")
        print(f"| Durability = {self.durability}|")
        print(f"| Attack     = {self.attack}|")
        print(f"| Agility    = {self.agility}|")
        print(f" ---------------")
        print(f"\n Special ability :-----------------------------------------")
        print(f"| Light. The magician can make monsters blind,             |\n"
              f"|and therefore always has 80% chance of escape from combat.|")
        print(f" ----------------------------------------------------------")