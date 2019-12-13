class Knight:

    def __init__(self):
        self.name = 'Knight'
        self.initiative = 5
        self.durability = 9
        self.attack = 6
        self.agility = 5
        self.type = 'hero'
        
    def ability_discription(self):
    
        print("\n1-Knight")
        print(f" ---------------")
        print(f"| Initiative = {self.initiative}|")
        print(f"| Durability = {self.durability}|")
        print(f"| Attack     = {self.attack}|")
        print(f"| Agility    = {self.agility}|")
        print(f" ---------------")
        print(f"\n Special ability :----------------------------------------------------")
        print(f"|The knight always blocks the first attack per battle with his shield,|\n"
              f"|and therefore need not avoid or take any damage                      |")
        print(f" ---------------------------------------------------------------------")

